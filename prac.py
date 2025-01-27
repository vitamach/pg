#pip install pandas openpyxl tqdm

import pandas as pd
import os
import re
from typing import List, Tuple, Dict, Optional
from tqdm import tqdm
from collections import defaultdict

def create_initial_files() -> Tuple[str, str]:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    input_file = os.path.join(data_dir, 'INPUT.xlsx')
    all_companies_file = os.path.join(data_dir, 'VSECHNY_FIRMY.xlsx')
    
    try:
        if not os.path.exists(input_file):
            pd.DataFrame({'Nazev_firmy': []}).to_excel(input_file, index=False)
        if not os.path.exists(all_companies_file):
            pd.DataFrame({'Nazev_firmy': []}).to_excel(all_companies_file, index=False)
    except Exception as e:
        print(f"Chyba při vytváření souborů: {str(e)}")
        raise
    
    return input_file, all_companies_file

def normalize_company_name(name: str) -> str:
    if pd.isna(name):
        return ""
    
    name = str(name).lower().strip()
    
    legal_forms = [
        's.r.o.', 'a.s.', 'k.s.', 'v.o.s.', 'spol.', 'sro', 'as', 'spol s r o',
        's r o', 'spol.s.r.o', 'společnost s ručením omezeným', 'akciová společnost',
        'komanditní společnost', 'veřejná obchodní společnost', 'z.s.', 'zs', 'o.p.s.',
        'ops', 'obecně prospěšná společnost', 'nadační fond', 'n.f.', 'nf', 'družstvo',
        'příspěvková organizace', 'p.o.', 'po', 'státní podnik', 's.p.', 'sp',
        'živnostník', 'osvč', 'sdružení', 'spolek', 'ústav', 'z.ú.', 'zu',
        'se', 'evropská společnost'
    ]
    
    for form in legal_forms:
        name = name.replace(form, '')
    
    name = name.replace('-', ' ')
    name = re.sub(r'\bcz\b', '', name)
    name = re.sub(r'cz-', '', name)
    
    chars_map = {
        'ě':'e', 'š':'s', 'č':'c', 'ř':'r', 'ž':'z', 'ý':'y', 'á':'a',
        'í':'i', 'é':'e', 'ú':'u', 'ů':'u', 'ň':'n', 'ť':'t', 'ď':'d',
        'ö':'o', 'ä':'a', 'ü':'u', 'ó':'o'
    }
    
    for old, new in chars_map.items():
        name = name.replace(old, new)
    
    name = re.sub(r'[^\w\s]', '', name)
    return ' '.join(name.split())

def analyze_word_structure(word: str) -> Dict:
    return {
        'length': len(word),
        'prefix': word[:3] if len(word) >= 3 else word,
        'suffix': word[-3:] if len(word) >= 3 else word,
        'chars': list(word)
    }

def compare_words(word1: str, word2: str) -> float:
    if word1 == word2:
        return 1.0
    
    struct1 = analyze_word_structure(word1)
    struct2 = analyze_word_structure(word2)
    
    score = 0.0
    
    prefix_len = min(len(struct1['prefix']), len(struct2['prefix']))
    if prefix_len > 0:
        matching_prefix = sum(1 for i in range(prefix_len) 
                            if struct1['prefix'][i] == struct2['prefix'][i])
        score += 0.4 * (matching_prefix / prefix_len)
    
    min_len = min(len(word1), len(word2))
    max_len = max(len(word1), len(word2))
    char_score = 0
    for i in range(min_len):
        weight = 1.0 if i < 3 else 0.5
        if word1[i] == word2[i]:
            char_score += weight
        elif i > 0 and i < min_len - 1:
            if word1[i] == word2[i+1] and word1[i+1] == word2[i]:
                char_score += weight * 0.5
    
    char_score = char_score / max(sum(1.0 if i < 3 else 0.5 for i in range(max_len)), 1)
    score += 0.4 * char_score
    
    length_diff = abs(len(word1) - len(word2))
    length_penalty = max(0, 1 - (length_diff / max(len(word1), len(word2))))
    score += 0.2 * length_penalty
    
    return score

def is_duplicate(name1: str, name2: str, threshold: float = 0.75) -> bool:
    if pd.isna(name1) or pd.isna(name2):
        return False
    
    name1_norm = normalize_company_name(name1)
    name2_norm = normalize_company_name(name2)
    
    if not name1_norm or not name2_norm:
        return False
    
    words1 = name1_norm.split()
    words2 = name2_norm.split()
    
    if len(words1) == 1 and len(words2) == 1:
        similarity = compare_words(words1[0], words2[0])
        return similarity >= 0.85
    
    word_matches = []
    for w1 in words1:
        best_match = max((compare_words(w1, w2) for w2 in words2), default=0)
        word_matches.append(best_match)
    
    avg_similarity = sum(word_matches) / len(word_matches)
    
    word_count_penalty = 1.0 - (abs(len(words1) - len(words2)) * 0.2)
    word_count_penalty = max(0, min(1, word_count_penalty))
    
    final_score = avg_similarity * word_count_penalty
    
    return final_score >= threshold

def create_company_index(companies: pd.Series) -> Dict[str, List[str]]:
    index = defaultdict(list)
    for company in companies:
        if pd.isna(company):
            continue
        normalized = normalize_company_name(company)
        if normalized:
            first_chars = normalized[:2].lower()
            index[first_chars].append(company)
    return index

def find_duplicates(company: str, company_index: Dict[str, List[str]], threshold: float = 0.75) -> List[str]:
    if pd.isna(company):
        return []
    
    normalized = normalize_company_name(company)
    if not normalized:
        return []
    
    first_chars = normalized[:2].lower()
    potential_matches = set()
    
    potential_matches.update(company_index.get(first_chars, []))
    
    for chars in company_index:
        if chars != first_chars and (chars[0] == first_chars[0] or 
           abs(ord(chars[0]) - ord(first_chars[0])) == 1):
            potential_matches.update(company_index[chars])
    
    duplicates = []
    for potential_match in potential_matches:
        if is_duplicate(company, potential_match, threshold):
            duplicates.append(potential_match)
    
    return duplicates

def process_batch(companies: pd.Series, company_index: Dict[str, List[str]], threshold: float = 0.75) -> Tuple[List[str], List[Tuple[str, str]]]:
    new_companies = []
    duplicate_pairs = []
    
    for company in companies:
        if pd.isna(company):
            continue
            
        duplicates = find_duplicates(company, company_index, threshold)
        
        if duplicates:
            duplicate_pairs.extend([(company, dup) for dup in duplicates])
        else:
            new_companies.append(company)
            
    return new_companies, duplicate_pairs

def process_companies(batch_size: int = 1000, similarity_threshold: float = 0.75):
    try:
        input_file, all_companies_file = create_initial_files()
        
        input_df = pd.read_excel(input_file)
        all_companies_df = pd.read_excel(all_companies_file)
        
        companies = input_df.iloc[:, 0]
        existing_companies = all_companies_df.iloc[:, 0] if not all_companies_df.empty else pd.Series([])
        
        company_index = create_company_index(existing_companies)
        
        total_new_companies = []
        total_duplicate_pairs = []
        
        num_batches = (len(companies) + batch_size - 1) // batch_size
        
        with tqdm(total=len(companies), desc="Zpracování firem") as pbar:
            for i in range(num_batches):
                start_idx = i * batch_size
                end_idx = min((i + 1) * batch_size, len(companies))
                batch = companies[start_idx:end_idx]
                
                new_companies, duplicate_pairs = process_batch(batch, company_index, similarity_threshold)
                
                total_new_companies.extend(new_companies)
                total_duplicate_pairs.extend(duplicate_pairs)
                
                pbar.update(len(batch))
        
        if total_new_companies or total_duplicate_pairs:
            output_rows = []
            if total_new_companies:
                output_rows.extend(['Nové firmy:', ''] + total_new_companies)
            if total_duplicate_pairs:
                if total_new_companies:
                    output_rows.extend(['', ''])
                output_rows.extend(['Duplicitní firmy:', ''])
                output_rows.extend([f"{pair[0]} -> {pair[1]}" for pair in total_duplicate_pairs])
            
            new_df = pd.DataFrame({'Nazev_firmy': output_rows})
            
            if total_new_companies:
                all_companies_df = pd.concat([all_companies_df, pd.DataFrame({'Nazev_firmy': total_new_companies})], ignore_index=True)
                all_companies_df = all_companies_df.drop_duplicates()
                all_companies_df.to_excel(all_companies_file, index=False)
            
            current_dir = os.path.dirname(os.path.abspath(__file__))
            data_dir = os.path.join(current_dir, 'data')
            new_file = os.path.join(data_dir, 'NOVY.xlsx')
            new_df.to_excel(new_file, index=False)
            
            pd.DataFrame({'Nazev_firmy': []}).to_excel(input_file, index=False)
            
            print(f'Nalezeno {len(total_new_companies)} nových firem')
            print(f'Nalezeno {len(total_duplicate_pairs)} duplicitních firem')
            if total_new_companies:
                print('Nové firmy byly přidány do VSECHNY_FIRMY.xlsx')
            print('Výsledky byly uloženy do NOVY.xlsx')
            print('Obsah INPUT.xlsx byl smazán')
        else:
            print('Žádné nové firmy nenalezeny')
            
    except Exception as e:
        print(f"Došlo k chybě: {str(e)}")
        raise

if __name__ == '__main__':
    process_companies()
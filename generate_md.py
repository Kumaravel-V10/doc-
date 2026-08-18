import pandas as pd
import sys
import os

excel_path = r'c:\Users\Agentassist\Downloads\doc-\Drop1-Final Consolidated US 5.xlsx'
output_path = r'C:\Users\Agentassist\.gemini\antigravity\brain\4fe74e06-0729-426c-bf9d-0f7ba86e4501\release_notes.md'

os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, 'w', encoding='utf-8') as f:
    f.write('# Release Notes\n\n')
    f.write('Date: 2026-08-18\n')
    f.write('Application Release: Drop 1\n\n')
    f.write('## 1. Introduction\n')
    f.write('This document outlines the features and user stories included in the Drop 1 release of the application. It consolidates user stories and provides detailed acceptance criteria for each item.\n\n')
    f.write('## 2. What\'s New (User Stories)\n\n')
    
    try:
        xls = pd.ExcelFile(excel_path)
        sheets_to_process = ['Drop1-US', 'User_Stories']
        for sheet_name in sheets_to_process:
            if sheet_name in xls.sheet_names:
                df = pd.read_excel(xls, sheet_name)
                f.write(f'### Source: {sheet_name}\n\n')
                id_col = 'Story ID' if 'Story ID' in df.columns else None
                title_col = 'Title' if 'Title' in df.columns else 'Summary' if 'Summary' in df.columns else None
                desc_col = 'UserStory' if 'UserStory' in df.columns else 'Description' if 'Description' in df.columns else None
                ac_col = 'Acceptance Criteria' if 'Acceptance Criteria' in df.columns else None
                feat_col = 'Feature' if 'Feature' in df.columns else None
                
                if not id_col:
                    continue
                df = df.fillna('')
                if feat_col:
                    grouped = df.groupby(feat_col)
                    for feature, group in grouped:
                        if feature:
                            f.write(f'#### Feature: {feature}\n\n')
                        for index, row in group.iterrows():
                            story_id = row[id_col]
                            if not story_id:
                                continue
                            story_title = row[title_col] if title_col else ''
                            f.write(f'##### {story_id}: {story_title}\n\n')
                            if desc_col and row[desc_col]:
                                f.write(f'**Description/User Story:**\n{str(row[desc_col]).strip()}\n\n')
                            if ac_col and row[ac_col]:
                                f.write(f'**Acceptance Criteria:**\n{str(row[ac_col]).strip()}\n\n')
                            f.write('---\n\n')
                else:
                    for index, row in df.iterrows():
                        story_id = row[id_col]
                        if not story_id:
                            continue
                        story_title = row[title_col] if title_col else ''
                        f.write(f'#### {story_id}: {story_title}\n\n')
                        if desc_col and row[desc_col]:
                            f.write(f'**Description/User Story:**\n{str(row[desc_col]).strip()}\n\n')
                        if ac_col and row[ac_col]:
                            f.write(f'**Acceptance Criteria:**\n{str(row[ac_col]).strip()}\n\n')
                        f.write('---\n\n')
    except Exception as e:
        f.write(f'Error: {e}\n')

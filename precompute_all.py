"""
    Finds example sentences for all keywords and stores them in the keyword_pages.ex_sentence table.

    Runtime:
    100%|█████████████████████████████████████████████████████████| 82685/82685 [11:30:03<00:00,  2.00it/s]
"""
import sys
sys.path.append('..')

from website_db_connect import db

from main import get_ranked_sentences

from tqdm import tqdm
import json


if __name__ == '__main__':
    cur = db.cursor()

    cur.execute("SELECT id, name FROM keyword")
    keyword_ts = cur.fetchall()


    # Insert into 'question' table
    pbar = tqdm(total=len(keyword_ts))
    num_complete = 0

    for kw_id, keyword in keyword_ts:
        res = get_ranked_sentences(keyword, 9)

        # print(keyword, '---', res)
        for q in res:
            cur.execute(
                "INSERT INTO ex_sentence (keyword_id, content) VALUES (%s, %s)", 
                [kw_id, q]
            )

        num_complete += 1
        pbar.update(1)

        if num_complete % 150 == 0:
            db.commit()
            # break
    

    db.commit()
    pbar.close()

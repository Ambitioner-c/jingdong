import csv
import os
import json


def get_filename(data_path):
    filename_list = os.listdir(data_path)

    return filename_list


def write_file(comment, save_path):
    comment_id = comment['id']
    comment_type = 'max'
    plus_available = comment['plusAvailable']
    creation_time = comment['creationTime']
    reply_count = comment['replyCount']
    useful_vote_count = comment['usefulVoteCount']
    score = comment['score']
    content = comment['content'].replace('\n', '').replace(',', '，').replace(' ', '')

    with open(save_path, 'a') as f:
        f_writer = csv.writer(f)
        f_writer.writerow([comment_id, comment_type, plus_available, creation_time,
                           reply_count, useful_vote_count, score, content])


def parse(filename, data_path, save_path):
    file_path = data_path + filename
    with open(file_path, 'r') as f:
        txt = f.read()
        txt_json = json.loads(txt)
        comments = txt_json['comments']
        for j in comments:
            write_file(j, save_path)


if __name__ == '__main__':
    # 数据路径
    my_data_path = '../data/Mac/'

    # 保存路径
    my_save_path = '../data/comment.csv'

    my_filename_list = get_filename(my_data_path)

    for i in my_filename_list:
        parse(i, my_data_path, my_save_path)

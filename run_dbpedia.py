# coding=utf-8
from main import main


if __name__ == "__main__":

    model_name = "BertOrigin"
    label_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
    data_dir = "/search/hadoop02/suanfa/songyingxin/SongWork/PaperDataset/dbpedia"
    output_dir = ".dbpedia_output/"
    cache_dir = ".dbpedia_cache"
    log_dir = ".dbpedia_log/"

    model_times = "model_1/"   # 第几次保存的模型，主要是用来获取最佳结果

    # bert-base
    bert_vocab_file = "/search/hadoop02/suanfa/songyingxin/pytorch_Bert/bert-base-uncased-vocab.txt"
    bert_model_dir = "/search/hadoop02/suanfa/songyingxin/pytorch_Bert/bert-base-uncased"

    # # bert-large
    # bert_vocab_file = "/search/hadoop02/suanfa/songyingxin/pytorch_Bert/bert-large-uncased-vocab.txt"
    # bert_model_dir = "/search/hadoop02/suanfa/songyingxin/pytorch_Bert/bert-large-uncased"

    if model_name == "BertOrigin":
        from BertOrigin import args

    elif model_name == "BertCNN":
        from BertCNN import args

    elif model_name == "BertATT":
        from BertATT import args

    elif model_name == "BertRCNN":
        from BertRCNN import args

    elif model_name == "BertCNNPlus":
        from BertCNNPlus import args

    main(args.get_args(data_dir, output_dir, cache_dir,
                       bert_vocab_file, bert_model_dir, log_dir),
         model_times, label_list)

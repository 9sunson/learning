import pandas as pd
import xmltodict
import json
from xml.etree import ElementTree
import sys
import shutil


def save_to_file(f_name, contents):
    f = open(f_name, 'w')
    f.write(contents)
    f.close()


def read_csv(path):

    # noinspection PyBroadException
    try:
        df = pd.read_csv(path, dtype=str)
        return df
    except Exception:
        return None


def read_xls(path):
    # noinspection PyBroadException
    try:
        df = pd.read_excel(path, dtype=str)
        return df
    except Exception:
        return None


def read_xml(path):
    # noinspection PyBroadException
    try:
        tree = ElementTree.parse(path)
        root = tree.getroot()
        xml_str = ElementTree.tostring(root, encoding='utf-8', method='xml')
        df_dict = xmltodict.parse(xml_str)
        df_dict_root = json.loads(json.dumps(df_dict))['root']
        df = pd.DataFrame.from_dict(df_dict_root)
        return df
    except Exception:
        return None


def read_txt(path):
    # noinspection PyBroadException
    try:
        df = pd.read_table(path,sep=',')
        return df
    except Exception:
        return None


def convert_csv(df, path, filename):
    # noinspection PyBroadException
    try:
        path_final = path + filename + '.csv'
        df.to_csv(path_final, sep=',', index=None)
        return 1
    except Exception:
        return 0


def convert_xlsx(df, path, filename):
    # noinspection PyBroadException
    try:
        path_final = path + filename + '.xlsx'
        df.to_excel(path_final, index=None)
        return 1
    except Exception:
        return 0


def convert_xls(df, path, filename):
    # noinspection PyBroadException
    try:
        path_final = path + filename + '.xls'
        df.to_excel(path_final, index=None)
        return 1
    except Exception:
        return 0


def convert_xml(df, path, filename):
    # noinspection PyBroadException
    try:
        path_final = path + filename + '.xml'
        df_dict = df.to_dict(orient='list')
        df_dict_root = {'root': df_dict}
        df_xml = xmltodict.unparse(df_dict_root, encoding='utf-8', pretty=True)
        save_to_file(path_final, df_xml)
        return 1
    except Exception:
        return 0


def convert_txt(df, path, filename):
    # noinspection PyBroadException
    try:
        path_final = path + filename + '.txt'
        df.to_csv(path_final, sep=',', index=None)
        return 1
    except Exception:
        return 0


def copy_to_target(source_path, target_path):
    # noinspection PyBroadException
    try:
        shutil.copy(source_path, target_path)
        return 1
    except Exception:
        return 0


if __name__ == '__main__':
    path_source = sys.argv[1]
    format_target = sys.argv[2]
    path_target = sys.argv[3]
    index_point = path_source.rfind('.')
    index_split = path_source.rfind('/')
    format_source = path_source[index_point + 1:]
    file_name = path_source[index_split+1:index_point]

    if format_source == 'csv':
        data = read_csv(path_source)

        if isinstance(data, pd.DataFrame):
            if format_target == 'xlsx':
                re = convert_xlsx(data, path_target, file_name)
            elif format_target == 'txt':
                re = convert_txt(data, path_target, file_name)
            elif format_target == 'xml':
                re = convert_xml(data, path_target, file_name)
            elif format_target == 'csv':
                re = copy_to_target(path_source, path_target)
            elif format_source == 'xls':
                re = convert_xls(data, path_target, file_name)
            else:
                re = 0

        else:
            re = 0

    elif format_source == 'xlsx':
        data = read_xls(path_source)
        if isinstance(data, pd.DataFrame):
            if format_target == 'csv':
                re = convert_csv(data, path_target, file_name)
            elif format_target == 'txt':
                re = convert_txt(data, path_target, file_name)
            elif format_target == 'xml':
                re = convert_xml(data, path_target, file_name)
            elif format_target == 'xlsx':
                re = copy_to_target(path_source, path_target)
            elif format_source == 'xls':
                re = convert_xls(data, path_target, file_name)
            else:
                re = 0
        else:
            re = 0

    elif format_source == 'txt':
        data = read_txt(path_source)
        if isinstance(data, pd.DataFrame):
            if format_target == 'xlsx':
                re = convert_xlsx(data, path_target, file_name)
            elif format_target == 'csv':
                re = convert_csv(data, path_target, file_name)
            elif format_target == 'xml':
                re = convert_xml(data, path_target, file_name)
            elif format_target == 'txt':
                re = copy_to_target(path_source, path_target)
            elif format_source == 'xls':
                re = convert_xls(data, path_target, file_name)
            else:
                re = 0
        else:
            re = 0

    elif format_source == 'xml':
        data = read_xml(path_source)
        if isinstance(data, pd.DataFrame):
            if format_target == 'xlsx':
                re = convert_xlsx(data, path_target, file_name)
            elif format_target == 'txt':
                re = convert_txt(data, path_target, file_name)
            elif format_target == 'csv':
                re = convert_csv(data, path_target, file_name)
            elif format_target == 'xml':
                re = copy_to_target(path_source, path_target)
            elif format_source == 'xls':
                re = convert_xls(data, path_target, file_name)
            else:
                re = 0

        else:
            re = 0

    elif format_source == 'xls':
        data = read_xls(path_source)
        if isinstance(data, pd.DataFrame):

            if format_target == 'xlsx':
                re = convert_xls(data, path_target, file_name)
            elif format_target == 'txt':
                re = convert_txt(data, path_target, file_name)
            elif format_target == 'csv':
                re = convert_csv(data, path_target, file_name)
            elif format_target == 'xml':
                re = convert_xml(data, path_target, file_name)
            elif format_source == 'xls':
                re = copy_to_target(path_source, path_target)
            else:
                re = 0
        else:
            re = 0

    else:
        re = 0

    print(re)

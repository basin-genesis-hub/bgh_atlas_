import sys
import glob, os

# fin = open('auth_template.html', "rt")
# data = fin.read()

# for file in glob.glob("**/*.html", recursive=True):
#     if file == 'auth_template.html':
#         continue
#     print(file)
#     data_new = data.replace('MMMM-path-placeholder', '_site/'+file)
#     fout = open(file, "wt")
#     fout.write(data_new)
#     fout.close()

path = os.getcwd()
print('path', path)
file_list = []
model_locations = {}

for file in glob.glob(path + "/_posts/*.md"):
    file_list.append(file)

for filename in file_list:
    print('nothing')
# print('filename:', filename)


# with open('model_locations.yaml', 'w') as f:
#     f.write("_posts/%s " % item)    
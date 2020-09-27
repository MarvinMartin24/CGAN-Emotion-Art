import pandas as pd
import numpy as np

# Import dataset
df = pd.read_csv("WikiArt-Emotions/WikiArt-Emotions-Ag4.tsv", error_bad_lines=False, sep='\t')

# Map emotion to more genrtics one & onlykeep ImageOnly (Map Art (image+title) to ImageOnly)
# agreeableness -> happiness
df['ImageOnly: happiness'] = np.where(df['ImageOnly: agreeableness']== 1, 1, df['ImageOnly: happiness'])
df['ImageOnly: happiness'] = np.where(df['Art (image+title): agreeableness']== 1, 1, df['ImageOnly: happiness'])

# agreeableness -> happiness
df['ImageOnly: sadness'] = np.where(df['ImageOnly: shame']== 1, 1, df['ImageOnly: sadness'])
df['ImageOnly: sadness'] = np.where(df['Art (image+title): shame']== 1, 1, df['ImageOnly: sadness'])

# anticipation -> neutral
df['ImageOnly: neutral'] = np.where(df['ImageOnly: anticipation']== 1, 1, df['ImageOnly: neutral'])
df['ImageOnly: neutral'] = np.where(df['Art (image+title): anticipation']== 1, 1, df['ImageOnly: neutral'])

# arrogance -> anger
df['ImageOnly: anger'] = np.where(df['ImageOnly: arrogance']== 1, 1, df['ImageOnly: anger'])
df['ImageOnly: anger'] = np.where(df['Art (image+title): arrogance']== 1, 1, df['ImageOnly: anger'])

# regret -> sadness
df['ImageOnly: sadness'] = np.where(df['ImageOnly: regret']== 1, 1, df['ImageOnly: sadness'])
df['ImageOnly: sadness'] = np.where(df['Art (image+title): regret']== 1, 1, df['ImageOnly: sadness'])

# disagreeableness -> anger
df['ImageOnly: anger'] = np.where(df['ImageOnly: disagreeableness']== 1, 1, df['ImageOnly: anger'])
df['ImageOnly: anger'] = np.where(df['Art (image+title): disagreeableness']== 1, 1, df['ImageOnly: anger'])

# disgust -> fear
df['ImageOnly: fear'] = np.where(df['ImageOnly: disgust']== 1, 1, df['ImageOnly: fear'])
df['ImageOnly: fear'] = np.where(df['Art (image+title): disgust']== 1, 1, df['ImageOnly: fear'])

# gratitude -> happiness
df['ImageOnly: happiness'] = np.where(df['ImageOnly: gratitude']== 1, 1, df['ImageOnly: happiness'])
df['ImageOnly: happiness'] = np.where(df['Art (image+title): gratitude']== 1, 1, df['ImageOnly: happiness'])

# humility -> shyness
df['ImageOnly: shyness'] = np.where(df['ImageOnly: humility']== 1, 1, df['ImageOnly: shyness'])
df['ImageOnly: shyness'] = np.where(df['Art (image+title): humility']== 1, 1, df['ImageOnly: shyness'])

# optimism -> happiness
df['ImageOnly: happiness'] = np.where(df['ImageOnly: optimism']== 1, 1, df['ImageOnly: happiness'])
df['ImageOnly: happiness'] = np.where(df['Art (image+title): optimism']== 1, 1, df['ImageOnly: happiness'])

# pessimism -> sadness
df['ImageOnly: sadness'] = np.where(df['ImageOnly: pessimism']== 1, 1, df['ImageOnly: sadness'])
df['ImageOnly: sadness'] = np.where(df['Art (image+title): pessimism']== 1, 1, df['ImageOnly: sadness'])

# trust -> happiness
df['ImageOnly: happiness'] = np.where(df['ImageOnly: trust']== 1, 1, df['ImageOnly: happiness'])
df['ImageOnly: happiness'] = np.where(df['Art (image+title): trust']== 1, 1, df['ImageOnly: happiness'])

# Map Art (image+title) to ImageOnly
df['ImageOnly: anger'] = np.where(df['Art (image+title): anger']== 1, 1, df['ImageOnly: anger'])
df['ImageOnly: fear'] = np.where(df['Art (image+title): fear']== 1, 1, df['ImageOnly: fear'])
df['ImageOnly: happiness'] = np.where(df['Art (image+title): happiness']== 1, 1, df['ImageOnly: happiness'])
df['ImageOnly: love'] = np.where(df['Art (image+title): love']== 1, 1, df['ImageOnly: love'])
df['ImageOnly: sadness'] = np.where(df['Art (image+title): sadness']== 1, 1, df['ImageOnly: sadness'])
df['ImageOnly: shyness'] = np.where(df['Art (image+title): shyness']== 1, 1, df['ImageOnly: shyness'])
df['ImageOnly: surprise'] = np.where(df['Art (image+title): surprise']== 1, 1, df['ImageOnly: surprise'])
df['ImageOnly: neutral'] = np.where(df['Art (image+title): neutral']== 1, 1, df['ImageOnly: neutral'])

# Remove useless columns
df = df.drop(columns=['Artist', 'Title', 'Year', 'Painting Info URL', 'Artist Info URL', 'ImageOnly: agreeableness', 'ImageOnly: anticipation', 'ImageOnly: shame', 'ImageOnly: arrogance', 'ImageOnly: regret', 'ImageOnly: disagreeableness', 'ImageOnly: disgust', 'ImageOnly: gratitude', 'ImageOnly: humility', 'ImageOnly: optimism', 'ImageOnly: pessimism', 'ImageOnly: trust', 'Ave. art rating', 'Is painting'])

# Remove useless columns where title info
df = df[df.columns.drop(list(df.filter(regex='itle')))]

# Rename cells
df['Face/body'] = df['Face/body'].replace(to_replace ="face", value ="_face")
df['Face/body'] = df['Face/body'].replace(to_replace ="body", value ="_body")
df['Face/body'] = df['Face/body'].replace(to_replace ="none", value ="_none")
df['Style'] = df['Style'].replace(['Modern Art','Post Renaissance', 'Renaissance Art', 'Contemporary Art', 'Contemporary Art,Modern Art', 'Modern Art,Post Renaissance Art'],['_Modern_Art','_Post_Renaissance_Art', '_Renaissance_Art', '_Contemporary_Art', '_Contemporary_Art', '_Post_Renaissance_Art'])

# Fill art witout emotion with neural
df['emotion']='' # to create an empty column

for col_name in df.columns:
  df.loc[df[col_name]==1,'emotion']= df['emotion'] + '_' + col_name.split(' ')[-1]

df = df[df.columns.drop(list(df.filter(regex='nly')))]
df['emotion'] = df['emotion'].replace(to_replace ="", value ="_neutral")

# Dataset emotion stats
print(df['emotion'].value_counts())
print(df.info())

df.to_csv('art_emotion.csv', sep=',')


# DOWNLOAD

#import ssl
#import cv2
#import pathlib
#import os
#
#
#ssl._create_default_https_context = ssl._create_unverified_context
#
#for index, row in df.iterrows():
#  print("{}".format(index))
#  try:
#    print(row['emotion'].split("_")[1])
#    filename = "/DATASET_EMOTION/"+ row['emotion'].split("_")[1] +"/" + row['ID'] + row['Style'] + row['Face/body'] + row['emotion'] + ".jpg"
#    p = pathlib.Path(filename)
#    if not p.is_file():
#      os.chdir("DATASET_EMOTION/"+ row['emotion'].split("_")[1])
#      print(row["Image URL"])
#      img = io.imread(row["Image URL"])
#
#      rgb_crop_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#      cv2.imwrite(row['ID'] + row['Style'] + row['Face/body'] + row['emotion'] + ".jpg", rgb_crop_img)
#    else:
#      print("EXIST")
#  except SocketError as e:
#    print("EXCEPT")
#    if e.errno != errno.ECONNRESET:
#        raise # Not error we are looking for
#    pass # Handle error here.

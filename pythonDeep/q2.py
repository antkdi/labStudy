from scipy.misc import imread,imsave,imresize

img = imread('./image/lena.png')

newim = imsave.save('./image/change.png',img)

type(img)

#plt.imshow(img)
#plt.show();


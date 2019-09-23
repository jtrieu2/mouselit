%% read .nrrd image

% file name
fileName = '/Users/victor/github/deep-graphs/victor/MICCAI_data/CHB_train/CHB_train_Case01/CHB_train_Case01_T2.nhdr';

% open as image
reader = nhdr_nrrd_read(fileName, true);
image = reader.data;

% get size
imgSize = size(image);

% show axial slice 200
figure;
imagesc(image(:,:,200));

%% crop out border

zeroIdx = image==0;

figure;
imagesc(zeroIdx(:,:,200));

% %% sub-sample with imresize3
% % B = imresize3(V,[numrows numcols numplanes]
% 
% newSize = [159, 207, 79];
% 
% subImage = imresize3(image, newSize);
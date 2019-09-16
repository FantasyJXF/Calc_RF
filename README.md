# Calc_RF
To calculate the receptive field of CNN

# Algorithm
The receptive field is defined as the region in the input space that a particular CNN’s feature is looking at (i.e. be affected by).  This line comes from [Medium](https://medium.com/mlreview/a-guide-to-receptive-field-arithmetic-for-convolutional-neural-networks-e0f514068807).

The algorithm comes from [here](http://shawnleezx.github.io/blog/2017/02/11/calculating-receptive-field-of-cnn/), and I add the dilation parameter of convolution.

The receptive field (RF) `l_k` of layer $k$ is:

<img src="http://latex.codecogs.com/gif.latex?l_{k}=l_{k-1}+\left ( \left ( f_{k}-1 \right )\ast \coprod_{i=1}^{k-1}s_{i} \right )/>

where `l_{k-1}` is the receptive field of layer `k-1`, `f_k` is the filter size (height or width, but assuming they are the same here), and $s_i$ is the stride of layer `i`.

The formula above calculates receptive field from bottom up (from layer 1). Intuitively, RF in layer $k$ covers `(f_k - 1) * s_{k-1}` more pixels relative with layer `k-1`. However, the increment needs to be translated to the first layer, so the increments is a factorial — a stride in layer `k-1`is exponentially more strides in the lower layers.

> Anyone could refer to [this website](https://fomoro.com/research/article/receptive-field-calculator) to calculate the receptive fields.

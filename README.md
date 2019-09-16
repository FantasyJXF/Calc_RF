# Calc_RF
To calculate the receptive field of CNN

# Algorithm
The receptive field is defined as the region in the input space that a particular CNN’s feature is looking at (i.e. be affected by).  This line comes from [Medium](https://medium.com/mlreview/a-guide-to-receptive-field-arithmetic-for-convolutional-neural-networks-e0f514068807).

The algorithm comes from [here](http://shawnleezx.github.io/blog/2017/02/11/calculating-receptive-field-of-cnn/), and I add the dilation parameter of convolution.

> Anyone could refer to [this website](https://fomoro.com/research/article/receptive-field-calculator) to calculate the receptive fields.

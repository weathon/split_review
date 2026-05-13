# PTNQ: Post-Training Non-Linear Quantization

- Decision: Reject
- Scores: 5, 3, 3

## Abstract
Quantization is one of the leading techniques to reduce the memory usage of machine learning models.
It works by approximating the weights of a model by some function with a smaller domain (e.g., replace 32-bit floats with 8-bit integers that are coefficients in some function that maps back to 32-bit floats).

Although most quantization methods approximate weights with a linear or affine function, the weights of current machine learning models often exhibit non-linear behavior at the extremities.
Moreover, some studies suggest that the extremities are important for the end-to-end accuracy.

In this paper, we introduce PTNQ, a novel post-training quantization technique that approximates weights by searching through a pool of non-linear functions.
We show that PTNQ provides significant advantages over affine functions, achieving similar accuracy while requiring 2 to 4 fewer bits per coefficient.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces Post-Training Non-Linear Quantization (PTNQ), that uses non linear functions to approximate the weights of a trained network. The technique has three components: 
1. Function selection - PTNQ evaluates a broad set of non linear functions (and their combinations up-to a user defined depth k) to find the function best suited to minimize loss. 
2. Quantization parameter initialization - The authors try three different initialization strategies for the parameters of the functions, namely, initializing all parameters to 1, sampling from a standard normal distribution with range [-1,1], and space search - a technique that starts by generating parameters from a large initial range and iteratively narrows the range. The parameter ranges are optionally refined using non-linear regression.
3. Quantization parameter training - After initialization, the quantization parameters are further trained to minimize the mean square error between original weights and their quantized-dequantized counterparts. The technique leverages different learning rate schedulers to optimize performance.

### Strengths
1. The paper is easy to follow and describes the various components of the proposed technique well.
2. The motivation is clear, and this is a relevant problem.
3. The technique does show compression advantage, however, comparison with other state of the art techniques from literature (some of which are mentioned in the related work section) is missing, making it hard to gauge the merits of the proposed non linear quantization.

### Weaknesses
1. The approach increases quantization time and is slower at inference compared to linear methods. 
2. The technique has been only investigated on smaller models. On LLama3, the results are not much better than affine and torchao but the time and memory required for PTNQ are both higher. 
3. PTNQ requires further hardware optimizations to fully leverage its non-linear functions in production settings.
4. Comparison with state of the art PTQ and QAT techniques from literature is missing in the tables.

### Questions
Can you share the details of the data used for training, and how many tokens were needed to train the quantization parameters?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In this paper, authors propose the PTNQ algorithm. In PTNQ, users can pre-define a list of non-linear quantization function and PTNQ would provide the best non-linear quantization function, de-quantization function and best parameters. In their experiments, they claim that PTNQ provides significant advantages over affine functions, achieving similar accuracy while requiring 2 to 4 fewer bits per coefficient.

### Strengths
Nonlinear quantization is a popular topic, especially when the data distribution in the tensor is not uniform. Nonlinear quantization often makes better use of resources and reduces the noise caused by quantization.

The authors provide a huge of experiments to estimate their methods.

### Weaknesses
This paper faces many fatal problems:

1.The motivation is not strong.
As mentioned in the article, the  significance of quantitation methods is to reduce both storage costs and computation time. The reduction in computation time depends on the increase in bandwidth benefits when data is loaded into different storage device after storage reduction. These are two goals to be achieved at the same time.  

The article unilaterally emphasizes the benefits of storage, which is untenable for nonlinear quantization raise the computation time dramatically. In practice, storage is a key point, but there are more effective solutions than quantitative methods to solve the problem of purity storage problem. For example, in the advertising recommendation business, the embedding layer often uses 7z compression method for storage, and uses GPU for decompression after loading into the GPU memory. Therefore, the motivation in the article is untenable 

The experiments in this paper also show this point. In table 4, the inference time of PTNQ is much larger than traditional linear quantization, but compared with linear quantization, the model size is not small significantly. 

2.The method is trivial and writing is poor.

The methods in this article are very trivial. A simple yet effective method is important factor to accept this paper. However, when describing the simple method, emphasis should be placed on describing other properties of the method, such as how it is effective and how it is important in real business, rather than detailing how it is initialized. Therefore, sections 2.1.1-2.1.3 of this article should be rewritten to reduce unnecessary descriptions and further analyze the effectiveness and rationality of the method. Therefore, this article has significant shortcomings in  paper writing.

### Questions
How to design nonlinear quantization methods that can simultaneously balance model size and computation time?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper introduces PTNQ, a novel quantization technique designed to reduce memory usage in machine learning models by utilizing non-linear functions rather than traditional linear or affine methods. It highlights the trade-offs of using non-linear functions over standard affine functions, showing a reduction in bits required without significant accuracy loss. This approach enables memory-efficient model deployment without compromising accuracy, making it particularly relevant for resource-constrained environments

### Strengths
1. PTNQ innovates by leveraging a pool of non-linear functions, allowing for more accurate weight approximation in neural networks while using fewer bits per coefficient.
2. PTNQ’s two-phase approach first generates and evaluates various non-linear quantization functions, then selects the optimal one.
3. PTNQ explores various initialization methods, learning rate schedulers, and function combinations, providing insights into the optimal settings for different models.

### Weaknesses
1. I think it is unfair to compare PTNQ with affine and torchao, as both are uniform quantization methods. A fairer comparison would involve other non-uniform quantization techniques.
2. In Table 4, the inference time for PTNQ increases significantly, while the memory savings and performance improvements appear minimal.
3. This method relies on multiple steps and various heuristic combinations to determine the optimal solution, which may limit its practicality for real-world applications.
4. In terms of academic writing, there is space for improvement in the paper’s logical flow and structural clarity.
5. The innovative aspects of this work seem somewhat limited and may not yet meet the competitive standards expected for ICLR.

### Questions
1. Which kind of specific quantization method do you use? Like GTPQ, AWQ?
2. What is the affine function, like f(x)=x? Can you give an example? As I understand, affine function is applied in uniform quantization and non-linear function is more suited in non-uniform quantization.
3. Which model specifically did you use in the experimental part? Like llama3-8b?

### Soundness
2

### Presentation
2

### Contribution
2

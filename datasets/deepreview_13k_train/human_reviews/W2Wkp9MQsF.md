# Forget the Data and Fine-Tuning! Just Fold the Network to Compress

- Decision: Accept
- Scores: 6, 6, 5, 6

## Abstract
We introduce model folding, a novel data-free model compression technique that merges structurally similar neurons across layers, significantly reducing the model size without the need for fine-tuning or access to training data. Unlike existing methods, model folding preserves data statistics during compression by leveraging k-means clustering, and using novel data-free techniques to prevent variance collapse or explosion. Our theoretical framework and experiments across standard benchmarks, including ResNet18 and LLaMA-7B, demonstrate that model folding achieves comparable performance to data-driven compression techniques and outperforms recently proposed data-free methods, especially at high sparsity levels. This approach is particularly effective for compressing large-scale models, making it suitable for deployment in resource-constrained environments.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes a new training- and fine-tuning-free method for neural network compression. Inspired by recent research on neuron alignment, in particular the weight matching algorithm [Ainsworth et al., 2023], the method essentially works by applying k-means vector quantization to cluster similar neurons (i.e., rows or channels of a weight matrix/tensor) together, and applying an additional data-free REPAIR (Jordan et al. (2022)) procedure to preserve the activation statistics of the original network. Experiments on convnets (e.g., ResNets, VGGs) demonstrate improved accuracy / sparsity tradeoff against other SOTA data-free pruning methods (e.g., FM (Chen et al., 2023), and INN (Solodskikh et al., 2023)). Experiment on an LLM (LLaMA-7B) shows comparable / somewhat worse performance than other pruning methods that require data/finetuning.

### Strengths
I think conceptually connecting the research and recent methods in neuron alignment / neural network symmetry (Yamada et al., 2023; Ainsworth et al., 2023) to the problem of model compression is somewhat novel and deserves more attention, although it certainly has been done many times, see e.g., [Zhou et al., 2018](https://arxiv.org/abs/1804.05862) and the paper [Chen et al., 2023](https://arxiv.org/pdf/2310.06756) cited in the current work. Methodologically the contribution seems fairly incremental (i.e., weight quantization, extension of the existing REPAIR (Jordan et al. (2022)) method).

The writing quality and clarity is mostly good; the experiments/figures are informative. 

I rate the significance as moderate. In terms of practical impact, the method is relatively easy to understand and implement, and obtains competitive performance among other data- and tuning-free approaches. However, I was hoping to see more in terms of bridging the conceptual understanding of neural network symmetry and compression, e.g., whether the proposed *model folding* method (essentially VQ) compares/relates to the weight matching of (Ainsworth et al., 2023), and whether it also enables some degree of alignment or mode connectivity b/w two randomly pretrained neural networks.

### Weaknesses
1. The paper is missing related literature and baselines on model quantization. A simple Google search suggests quite a few related papers, e.g., using vector quantization for model compression [[Martinez et al., 2021]](https://openaccess.thecvf.com/content/CVPR2021/papers/Martinez_Permute_Quantize_and_Fine-Tune_Efficient_Compression_of_Neural_Networks_CVPR_2021_paper.pdf) and post-training quantization [[Nagel et al., 2021](https://arxiv.org/pdf/2106.08295)] which is also training-free.

2. Some of the writing can be improved:
  - The section on Fold-AR is a bit hard to understand; it's unclear what exactly is being proposed. Perhaps an algorithm box can help.
  - The paper repeatedly talks about "merging similar channels" as the basis of the model folding algorithm, without defining it for various network architectures considered (especially outside the context of CNNs). This should be clarified, as how the scalar weights are grouped into vectors can have a big performance impact on VQ.
  - Some typographical errors: Line 278: "The variance ratio of the l-the", "l-the" -> "l-th"; unfinished sentence on Line 414: "Fold-DIR ourperforms Fold-AR as the cost of generating a batch of synthetic images and a forward pass through the network."

### Questions
As mentioned earlier, I find the connection between weight matching (Ainsworth et al., 2023) and the proposed VQ method to be somewhat lacking, and the former seems more like an inspiration on which the method is loosely based. Do the authors suspect a similar effect of alignment to be achieved through quantization, such that distant modes can be connected with low loss barrier in between them (as in (Ainsworth et al., 2023))?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper presents Model Folding, a data-free and fine-tuning-free model compression technique that merges structurally similar neurons within a neural network. This approach contrasts with traditional methods that often require access to training data or fine-tuning after compression.  Experiments on standard benchmarks, including ResNet and large models like LLaMA-7B, show that Model Folding achieves high sparsity while maintaining competitive performance with data-driven methods and outperforming recent data-free compression techniques.

### Strengths
1. The method has both theoretical justification and empirical support, demonstrating that k-means clustering is an optimal method for weight fusion in a data-free manner. Results from benchmarks like ResNet18 and LLaMA-7B show that model folding achieves performance on par with or surpasses existing data-driven and data-free compression methods, particularly at high sparsity levels.

2. Model folding is designed to be completely data-free, which differentiates it from other compression methods that typically require fine-tuning with original data. The authors propose two data-free alternatives for adjusting internal data statistics—Fold-AR and Fold-DIR—based on approximate and deep inversion-based techniques. It presents significant improvements over existing state-of-the-art data-free methods, demonstrating its applicability in compressing large-scale models effectively

### Weaknesses
1. More data-free and training-free references are needed, such as [1]

2. Lack of sufficient experimental results on compression ratio and speedup ratio.

### Questions
1. Is there a speed comparison of inference on different devices after compression of the model?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a data-free and fine-tuning-free method for compressing deep neural networks. This is achieved by identifying and merging redundant parameters through a similarity-based approach, followed by data generation with DeepInversion for further repair. The method is flexible and can be applied to both vision models like ResNet by merging channels and LLMs by merging linear weights, demonstrating effectiveness across different architectures. Extensive experiments on ImageNet, CIFAR-10, and CIFAR-100 highlight the method's robustness, with results clearly illustrated through figures.

### Strengths
1. Previous methods typically rely on data-driven fine-tuning to restore the performance of compressed models. This paper addresses this limitation by introducing a data-free method that leverages generated data and an efficient activation repair process to recover model accuracy, making it highly practical for real-world applications.
2. The paper includes extensive experiments on both vision and language models, with clear visualizations and figures that offer detailed insights into the method's performance. Notably, at high sparsity levels (>40%), the proposed method achieves significantly better accuracy compared to prior baselines, such as IFM and INN.
3. The presentation is good, with a clear illustration of the entire pipeline in Figure 1. Additionally, the method is straightforward to implement and highly reproducible.

### Weaknesses
1. My main concern with this submission is the limited technical novelty. The work largely combines existing methods, including similarity-based model merging for compression [1], model inversion for data generation [2], and REPAIR [3] for statistics alignment. While these components are integrated effectively, the key contributions could be further emphasized to distinguish this work. Specifically, the method uses k-means clustering for identifying redundant parameters, which is a well-established technique, and the subsequent merging of these parameters based on similarity is also not novel. The core of the method relies on DeepInversion for data generation, which is then used to repair the model's activations. This combination, while functional, does not introduce a fundamentally new approach to model compression.
2. Although the paper claims the method is data-free, this feature is primarily enabled by DeepInversion rather than a new development within this work. Clarifying the unique aspects of this approach compared to existing data-free methods would strengthen the contribution. The paper should more clearly articulate what differentiates its data-free approach from other methods that also use generated data for model repair. The reliance on DeepInversion as the primary driver for the data-free aspect diminishes the novelty of the method itself. A more detailed analysis of how the method's specific implementation of DeepInversion differs from standard applications would be beneficial.
3. The folding results on LLaMA-7B are not particularly competitive, with a Wiki PPL of 13.33, compared to other pruning methods like LLM-Pruner (PPL=10.53) and Wanda (PPL=8.22). The claim that "model folding achieves comparable performance to data-driven methods" may be overstated due to this significant gap in PPL. The paper needs to acknowledge this performance gap more explicitly and provide a more nuanced discussion of the limitations of the method when applied to large language models. The current presentation suggests a level of parity that is not supported by the experimental results.
4. SliceGPT [4], which similarly merges parameter matrices via a learnable transformation matrix, is another "merging"-based method and should be considered as a relevant baseline for comparison. The paper should include a comparison with SliceGPT to better contextualize the performance of the proposed method within the landscape of merging-based compression techniques. The absence of this comparison leaves a gap in the evaluation of the method's effectiveness.

### Questions
Please see weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a method to merge the columns in the weight matrix in a data-free manner. The method is composed of two parts: first, using the clustering method to find and merge the weight matrix. Then, based on the observation that the variance ratio after compressing the model would collapse or overshooting, the authors propose the data-free Fold-AR and Fold-DIR to inverse the model and repair the model. Experiments show that the proposed method can achieve better results than previous data-free methods, especially at high sparsity ratio.

### Strengths
1. Rigorous theoretical analysis of the proposed method
2. A comprehensive framework for merging and repairing the model under the data-free setting, also without fine-tuning.
3. The writing of the paper is good

### Weaknesses
1. There are plenty of works [1,2,3,4] about how to compress the model under the data-free setting, including the DeepInversion, which is mentioned as part of the method in this paper. These papers are all not mentioned and compared in the paper.
2. The experimental results show that the authors’ proposed methods experience significant performance drops compared to finetuning-based methods. Given that the cost of finetuning remains acceptable but the performance drop is not neglectable, it’s unclear why a tuning-free setting is necessary (since we can get the synthetic by methods like DeepInversion).
3. For methods on LLaMA, [5] also propose a model merging method to compress the model without fine-tuning. Please compare to this paper.

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2

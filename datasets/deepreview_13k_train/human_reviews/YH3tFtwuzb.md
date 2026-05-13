# Differentially Private Bias-Term Fine-tuning of Foundation Models

- Decision: Reject
- Scores: 8, 3, 5, 6, 5

## Abstract
We study the problem of differentially private (DP) fine-tuning of large pre-trained models -- a recent privacy-preserving approach suitable for solving downstream tasks with sensitive data. Existing work has demonstrated that high accuracy is possible under strong privacy constraint, yet requires significant computational overhead or modifications to the network architecture.
We propose differentially private bias-term fine-tuning (DP-BiTFiT), which matches the state-of-the-art accuracy for DP algorithms and the efficiency of the standard BiTFiT. DP-BiTFiT is model agnostic (not modifying the network architecture), parameter efficient (only training about $0.1\%$ of the parameters), and computation efficient (almost removing the overhead caused by DP, in both the time and space complexity). On a wide range of tasks, DP-BiTFiT is $2\sim 30\times$ faster and uses $2\sim 8\times$ less memory than DP full fine-tuning, even faster than the standard full fine-tuning. This amazing efficiency enables us to conduct DP fine-tuning on language and vision tasks with long-sequence texts and high-resolution images, which were computationally difficult using existing methods.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work studies a differentially private version of bitfit, termed DP-Bitfit. DP-bitfit, like bitfit, works by tuning only the bias terms in the model. However, the key innovation here is recognizing that bitfit is highly parameter efficient which is crucial for DP learning. Second, is recognizing that the gradients are much computationally cheaper to calculate due to it being activation-free. Overall, this work shows impressive empirical results evaluated on both image and text models.

### Strengths
Overall, this work shows to be a strong submission. This work includes comprehensive comparison between different existing methods (e.g., ghost clipping) and shows impressive benefits in both memory, throughput, and final model utility. It is perhaps unsurprising that this performs so well given the performance of non-DP bitfit, however, the core benefit of this work is recognizing its potential for the DP setting.

The organization of the work is clear, and the work includes several key figures and diagrams that help the reader follow the work. For example, Figure 1 clearly shows the empirical benefits of the approach and Section 3/ Figure 2 the  asymptotic benefits.

Though the novelty is lower because this is essentially applying DP-SGD to the existing "bitfit" algorithm, this work include smany empirical results evaluated across different model families (e.g., ViT models,resnets, and roberta models) on both text and image classification as well as text generation.

### Weaknesses
This works lacks a clear empirical exploration of the difference between the activation and the model memory. Right now, it is clear that the algorithm uses much less memory and compute. However, it is unclear how the total memory in figure 1 is split between storing the model, materializing activations, and other overheads like optimizer states. A more detailed breakdown of memory consumption would be beneficial, perhaps showing the memory footprint of the base model, the trainable parameters, and the activation maps separately for different model sizes. This would help in understanding the exact source of the memory savings and how it scales with model size.

Figure 4 is extremely confusing. How can DP-BITFIT be both on the x-axis and in the legend? What does maximum through of algorithm mean? The figure needs a clearer explanation of what is being plotted. Specifically, the x-axis label is ambiguous, and the meaning of 'maximum throughput' needs to be defined more precisely. Is it the maximum throughput achieved during training or some other measure? The use of DP-Bitfit as a reference line is also not immediately clear, and the figure would benefit from a more detailed caption explaining how to interpret the slopes and the relative positions of the different methods.

### Questions
In table 5, how were the results of Bu et al. obtained? I could not find any 98.9% performance (Cifar-10 result) in their work.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the problem of differentially private (DP) fine-tuning of large pre-trained models. Existing research has shown that high accuracy can be achieved under strong privacy constraints, but it often comes at the cost of significant computational overhead or modifications to the network architecture.

The authors propose  "differentially private bias-term fine-tuning" (DP-BiTFiT)  to strike a balance between accuracy and efficiency. DP-BiTFiT achieves state-of-the-art accuracy levels for DP algorithms while maintaining the efficiency of standard BiTFiT (fine-tuning without privacy constraints). The efficiency enables the application of DP fine-tuning to language and vision tasks involving long-sequence texts and high-resolution images, which were previously computationally challenging using existing methods.

### Strengths
Efficiency and Scalability: The paper presents an efficient and scalable approach to differentially private fine-tuning, which is crucial for handling large models and complex tasks. Compared with existing parameter-efficient DP fine-tuning, DP-BiTFiT is model-agnostic, i.e., it does not require modifications to the network architecture. The paper demonstrates that DP-BiTFiT outperforms DP full fine-tuning in terms of speed and memory usage, even surpassing the efficiency of standard full fine-tuning. 

Practical Applicability: The ability to conduct DP fine-tuning on language and vision tasks with long-sequence texts and high-resolution images expands the practical applications of privacy-preserving machine learning.

### Weaknesses
 **Limited contribution** Although the paper emphasizes that DP-BiTFiT is not merely adding differential privacy to an existing method (BiTFiT), it is hard to find much evidence for this point. Removing the forward hook is quite natural as one does not have to compute the gradient on weights. This is a natural choice when combining BiTFiT and differential privacy. Given existing results of DP full fine-tuning and parameter-efficient fine-tuning, the contribution of this paper is rather incremental. The core idea of only updating bias terms while applying DP is not particularly novel, as it aligns with the broader trend of parameter-efficient fine-tuning techniques that aim to minimize the number of updated parameters for efficiency. The paper does not adequately demonstrate a significant departure from these existing methods in terms of algorithmic innovation. Furthermore, the empirical evaluation shows performance drop of DP-BiTFiT compared with other parameter-efficient fine-tuning techniques. This performance gap raises questions about the practical utility of the proposed method, especially when compared to other parameter-efficient DP methods that achieve better accuracy. The paper mentions that DP-BiTFiT is efficient for a wide range of tasks, but it would be helpful to provide specific examples and use cases to illustrate its versatility. The lack of concrete examples makes it difficult to assess the practical impact of the proposed approach across diverse applications.

### Questions
1. In the Contribution 4, "DP-BiTFiT is a unique algorithm in that the computation overhead is independent of the feature dimension T" where T is the sequence length. The author should be more specific for this claim.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies private fine-tuning of large models using a parameter-efficient method. This work proposes DP-BitFit, differentially private bias-term fine-tuning, which updates bias terms during training under the DP-SGD framework.

While updating full parameters in DP-SGD would increase memory consumption and slow down the training process, DP-BitFit only needs to update 0.1% of the parameters, making it much faster than updating all parameters. This work supports this claim by providing both the time and space complexity and experimental comparisons. Another advantage of DP-BitFit is that it does not require a forward hook.

This work conducts experiments on both NLP tasks and computer vision (CV) tasks, considering privacy constraints within the ranges of [3, 8] for NLP and [1, 8] for CV.

### Strengths
1. The paper is well-motivated and easy to follow. Specifically, the theoretical analysis of space and time complexity of different methods is comprehensive. 

2. The experiments include both cv and nlp tasks, that are two of the main applications of foundation model use. The evaluation is comprehensive and ablates the model size, mode architectures, privacy levels.

### Weaknesses
1. My main concern with this paper is the novelty of this method. It appears that this method directly adapts the existing method BitFit to the DP-SGD. 

2. The performance of DP-BitFit is limited in some scenarios and requires the additional design for two phases, which makes the results of DP-BitFit less significant.

Minors:
1. Presentation issues: The table number and title should appear before the table (Table 7- 16). It would be better to be more careful with the use \citep and \citet.

### Questions
1. In Table 4, it is somewhat weird to me that the perplexity of non-private results is worse than private results in several cases. Also, Table 4 and Table 13 show that DP-BitFiT on GPT2-large is better than DP-BiTFiT is better than DP-SGD(full), I wonder if this is due to the dimensionality issue in DP-SGD, or sub-optimal hyperparameters for DP-SGD (full), or if it is because the comparison is not averaged across several runs for statistical significance.  

2. Comparison with DP parameter efficient methods for efficiency. The authors provide the theoretical comparison of DP-BitFit with other DP parameter-efficient methods. Figure 3 and Figure 4 compared the memory, speed, maximum throughput and batch size for DP-BitFit and full parameter updating methods. It would be better to also include the comparison to other DP parameter efficient methods such as DP-LoRA.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the differentially private fine-tuning of large pre-trained models. The key novelty of the paper is that the authors show that fine-tuning only the bias term can match or even outperform the SOTA DP fine-tuning algorithm in different tasks. By such bias-term fine-tuning idea, the number of trainable parameters can be even smaller than previous parameter-efficient fine-tuning methods (e.g., LORA), and faster and more memory-efficient than the full-parameter DP fine-tuning.

### Strengths
1. The paper presents the key idea with detailed and persuasive motivation.
2. The idea proposed in this paper can bring significant advantages in reducing computation costs while improving model utility.
3. The authors demonstrate relatively comprehensive experiments to support the claim advantages, including text classification, natural language generation, and image classification.

### Weaknesses
The paper is pretty much self-contained, there may be only some concerns on how general this method can be.
1. The paper can provide more intuitions about why fine-tuning the bias term can be effective enough with pre-trained models. As a comparison, LoRA is supported by a strong intuition that fine-tuning updates can be considered low-ranks.  
2. The limitation of the proposed algorithm may deserve some more discussion. While remark 4.2 mentioned that the method may be less effective for models with convolutional layers without bias terms, it is not clear whether all modules' bias terms (attention, fully connected, convolutional, etc.) have the same effect or some of them are more important than others. Besides, as some recent LLM architecture may not include biases in some layers (PaLM [0]) to increase training stability, it is unclear how general the proposed method can be in practice.

### Questions
1. Is there any potential limitations of the proposed algorithm in terms of the fine-tuning tasks? Can we expect similar improvement if we fine-tune for more complicated tasks, for example fine-tune LLaMA for GSM8k or for MMLU tasks?
2. Is there any requirement or conclusion about how well-pre-trained a model should be or how complex a model should be so that the proposed method can be effective? An inappropriate extreme example might be that one should not expect tuning the bias in a linear model to fit arbitrarily shifted distribution.
3. Maybe related to the above question, is there intuition to support the proposed method?
4. Are the bias terms in different modules (attention, fully connected, convolutional, etc.) have the same effects?

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper describes how to perform BitFit parameter-efficient fine-tuning of bias terms only with the addition of noise for differential privacy. BitFit is known to be effective and very parameter efficient, and it works well with DP because the number of trained parameters is so low.

### Strengths
A strong case is made for using the combination of BitFit and DP-SGD. The memory and time savings are efficient, both in theory and according to the extensive experiments. It feels somewhat incremental, but the experimental contribution demonstrating that the comination works well is still significant.

### Weaknesses
Contrary to the claims in the paragraph "novelty", it seems to me there is not a huge creative leap in putting together BitFit and DP-SGD as is done here. Is there something I am missing? What is the "substantial algorithmic innovation"? What is the naive way of combining these ideas that your algorithm improves upon?

The writing is unclear in places:
* The authors should study how to use \citep and \citet appropriately.
* Why is $C_i$ given as an input to Algorithm 1? I wonder if you mean the clipping function $C$.

I don't understand why you cannot combine with ghost clipping. The paragraph you mentioned says that they are "orthogonal", which to me sounds like they can both be used and each be beneficial. In what sense does ghost clipping "only work on the weights"? It scales the entire gradient, weights and biases alike.

I still think it is incorrect and misleading to count the number of "operations" without big O notation. It is not meaningful to say that "the total time complexity is $3Bp$". For example, you are considering taking a square (a multiplication) to be equivalent to summing (an addition). These operations may take different amounts of time, which is why we usually hide the constants behind the big O. Furthermore, as I tried to allude earlier, finding the sum of $n$ elements requires fewer than $n$ additions. To say "big O notation is an asymptotic symbol hence not precise" has it precisely backwards: big O conveys what is important (asymptotic behavior) while supressing what is unimportant (whether an addition or multiplication operation takes longer).

I don't understand what you mean "the bias gradients do not need the output gradient". All of the parameters' gradients depend on the output: it's only via the output that a parameter has any influence on the loss. You even say in the paper "the output gradient is used to compute the per-sample gradient of weights and biases". What am I misunderstanding?

### Questions
* See question about novelty above.
* Is this any better from a clipping perspective? Do you have to materialize the per-example bias gradients in order to compute their norms? You could combine this with ghost clipping, right?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

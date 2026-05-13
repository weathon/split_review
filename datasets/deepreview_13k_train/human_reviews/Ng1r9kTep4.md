# Inverted Activations: Reducing Memory Footprint in Neural Network Training

- Decision: Reject
- Scores: 8, 5, 6

## Abstract
The scaling of neural networks with increasing data and model sizes necessitates the development of more efficient deep learning algorithms. 
    A significant challenge in neural network training is the memory footprint associated with activation tensors, particularly in pointwise nonlinearity layers that traditionally save the entire input tensor for the backward pass, leading to substantial memory consumption.
    
    In this paper, we propose a modification to the handling of activation tensors in pointwise nonlinearity layers. 
    Our method involves saving the output tensor instead of the input tensor during the forward pass. Since the subsequent layer typically also saves its input tensor, this approach reduces the total memory required by storing only one tensor between layers instead of two. This optimization is especially beneficial for transformer-based architectures like GPT, BERT, Mistral, and Llama.

    To enable this approach, we utilize the inverse function of the nonlinearity during the backward pass. As the inverse cannot be computed analytically for most nonlinearities, we construct accurate approximations using simpler functions. 
    Experimental results demonstrate that our method significantly reduces memory usage without affecting training accuracy or computational performance.

    Our implementation is provided as a drop-in replacement for standard nonlinearity layers in the PyTorch framework, facilitating easy adoption without requiring architectural modifications. The code is available at \url{https://github.com/removed/for/anonimity}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes a method, called InvAct, to reduce the memory footprint associated with activation tensors during neural network training by modifying how activation tensors are saved for the backward pass in pointwise nonlinearity layers like GELU and SiLU.
Considering a block of two layers, instead of saving the input tensor for each layer, the authors suggest storing the output tensor of layer 1, which is the input tensor of layer 2. Then during the backward pass the input layer of layer 1 is reconstructed using the inverse of the nonlinearity. Since the nonlinearities considered in the paper do not have straightforward analytical inverses, the paper approximates the inverse functions using simpler functions. The paper shows great deal of memory savings for Transformer based architecture, around 25%, without noticeable impact on accuracy or computational efficiency, and can be used as a drop-in replacement for existing nonlinearity layers in PyTorch.

### Strengths
- **Originality**: The approach introduces a novel solution to the memory bottleneck in neural networks training. The proposed solution is straightforward yet impactful adjustment for deep learning workflows.
- **Clarity**: The method is clearly outlined, with pseudocode, detailed experimentation, and well written text.
- **Significance**: The reduction of memory footprint in training aligns well with current trends in model scaling. The method's compatibility with widely-used architectures and frameworks adds further value, especially for resource-constrained training environments.

### Weaknesses
 - **Experimental Scope**: The evaluation is limited to a few model architectures (BERT and LLama) and tasks (e.g., BERT fine-tuning on Yelp Reviews). Adding results from multiple tasks, such as [GLUE](https://huggingface.co/datasets/nyu-mll/glue), would strengthen claims of general applicability and robustness across varied scenarios.
- **Reporting of Experimental Details**: 
Including the fine-tuning details for the results reported in Sections 3.2 and 3.3, perhaps in the appendix could benefit the readers and help future research with reproducing the results reported in the paper.
- **Lack of Task-Specific Performance Metrics**: The results shown in Section 3.2 focus on training/validation loss without reporting task-specific metrics (e.g., accuracy, F1 score for Yelp Reviews). Including such metrics would better contextualize the impact of approximation errors on model quality.
- **Lack of Performance Evaluation for Other Models**: Although memory savings are reported for models like the Audio Spectral Transformer, ViT, and CLIP, no experimental analysis is provided to assess if or how these savings impact model performance. For instance, similar to the BERT and Llama evaluations in Sections 3.1 and 3.2, experiments could show if the method affects performance metrics and how much computational overhead is introduced for these models. Furthermore, in the abstract, the authors mention models like *GPT* and *Mistral* as potential beneficiaries of the method, yet there is no experimental data on memory savings, time overhead, or performance impact for these models. Including analysis or removing these model names would provide a more accurate representation of the paper's scope.

**P.S.**: I am more than willing to raise my score if the concerns mentioned in the **Weakness** and **Questions** section are addressed.

### Questions
1. **Sample Size and Standard Deviation**: Are the results in Table 1 averaged over multiple trials? If so, what is the sample size and standard deviation?  If the results show metrics over only a single run, then reporting the results over multiple runs with reports on the standard deviations would better highlight robustness and reproducibility of the method.
2. **Precision Bit InvAct**: I am curious to know if you have performed any performance evaluation as seen in Sections 3.2 and 3.3 on Precision Bit InvAct. The results presented in Table 1 suggest this variant to have less overhead but it is not clear how much error it produces in downstream tasks.
3. **Clarification on Experimental Consistency**: For the FewBit comparison in Figure 5, was the same dataset used as in Section 3.2? If different datasets were used, specifying this in Section 3.3 would enhance clarity.
4. **Sequence Length in BERT Experiment**: In Appendix A.3, the experiment setup for BERT specifies a sequence length of 1024, which exceeds the model’s typical limitation of 512 tokens. Could you clarify how this was achieved? Was a specific technique used to expand the sequence limit to 1024? If so please share more details.
## Minor suggestions:
1. **Additional Details Needed in Listing 1**: In Listing 1, memory savings for the Llama model are not shown, despite Llama being used in Section 3 for performance analysis. Including this information would create a more comprehensive view of the memory savings achievable with this approach.
2. **Sentence Rewrite in Line 464**: In the sentence, "Former are used more in during inference," the word "in" is unnecessary. The corrected sentence should read:  
  > "Former are used more during inference."

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This article presents a modification to the GELU and SiLU activations to save the output tensor instead of the input, recomputing the input to save approximately a quarter of the memory overhead in practice. They provide several variants of their method, all revolving around the idea of dividing the activation function into monotonous parts which can be inverted. They measure extensively that their approach does not change the computation time and doesn't affect performance.

### Strengths
- The method proposed is simple and only requires a drop-in replacement of the activation functions, providing a major memory improvement.
- The proposed inversion methods are novel, notably the approximate inverses of the GELU and SiLU functions.
- The computational efficiency of the method is considered on many different frameworks.
- The paper is clear and well-presented.

### Weaknesses
 - The main method proposed has very limited novelty outside of the consideration of GELU and SiLU. Other approaches have already proposed inverting the computations of the activation function such as [1] for similar reasons reducing the memory by half and with further benefits.
- At no point comparison with activation/gradient checkpointing is considered, despite the method being extremely similar. Indeed, why not simply store the input tensor only and recompute the output of the activation for efficient gradient computation? This is the same method, but it doesn't require an approximate inversion like proposed here. An extensive literature on checkpointing is necessary to consider here to compare the proposed method to, such as [2-4]. Notably, [5] has a particular consideration for the forward and backward of GeLU. It seems very hard to justify this method compared to more standard checkpointing methods, which computes an optimal trade-off between activation and computation time.
- The approximation error of the derivative of the inverse as represented in Figure 2 shows a non-negligible error for values of $x$ close to 0, which seems a bit worrying.
- Other activation functions are not considered. How is ReLU supposed to work in this framework?

### Questions
- How were the coefficients $c_i$ obtained ?
- Why is there an increase in execution time for InvAct only for the Plain GELU? What about the execution time for SiLU?
- The Sign-bit Inverted activation should be explained more clearly.
- Figure 3 requires labels for the rows and columns to be more clear.

**Minor details**

- The abstract in the openreview summary has a formatting error.
- line 182 "based"
- line 701 "assstance"

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper derives a method that reduces the amount of data that has to be stored in memory during the forward pass for the backpropagation. By doing so, it is possible to save a significant amount of memory during the training of a neural network. The proposed method is easily implementable and can be deployed in a training procedure with almost no impact
+ on the training duration,
+ on the overall performance of the model,

as it is supported by experimental results.

### Strengths
+ The proposed method is derived from a very simple idea, yet it leads to substantial reduction in memory costs, without introducing significant drawbacks or trade-offs (in particular it has no significant impact on either the training time or the model's performance)
+ The method is explained in a very clear way, as well as the research objectives of the paper
+ Thanks to its simplicity, the method is likely implementable within existing frameworks, without changing their core functioning

### Weaknesses
The main weeknesses of the paper lie in its experimental section:
+ Some claims of the paper are not supported by experiments, such as line 60: "effectively reducing the memory footprint by nearly $25\%$ in practice", it would be nice to see empirical evidence of such a claim
+ More generally, no experiment on the memory footprint achieved by the proposed method is shown, yet since the main objective of the paper is apparently to reduce the memory footprint during training, the paper would benefit greatly from such results
+ In section 3.1, the authors use two different frameworks to assess the computational efficiency of their method, but it seems thus difficult to have a clear view on whether the observed gap in computational efficiency is due to the authors method, or to the fact that two different frameworks are being used
+ Finally, could the authors add a theoretical example of how in practice the proposed method would allow to discard some tensors for back propagation computation would make the contribution of the paper more striking

### Questions
+ The authors claim that the studied activations are chosen because they are popular choices for transformers, did the authors try to apply their methods to other activations / nonlinearities ?
+ There is a tipo at line 337 ("implementatoins")

### Soundness
2

### Presentation
3

### Contribution
4

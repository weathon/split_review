# Revisiting Convolution Architecture in the Realm of DNA Foundation Models

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
In recent years, A variety of methods based on Transformer and state space model (SSM) architectures have been proposed, advancing foundational DNA language models. 
However, there is a lack of comparison between these recent approaches and the classical architecture—convolutional networks (CNNs)—on foundation model benchmarks.
This raises the question: are CNNs truly being surpassed by these recent approaches based on transformer and SSM architectures? In this paper, we develop a simple yet well-designed CNN-based method, named ConvNova. ConvNova identifies and proposes three effective designs: 1) dilated convolutions, 2) gated convolutions, and 3) a dual-branch framework for gating mechanisms. 
Through extensive empirical experiments, we demonstrate that ConvNova significantly outperforms recent methods on more than half of the tasks across several foundation model benchmarks. For example, in histone-related tasks, ConvNova surpasses the second-best method by an average of 5.8\%, while generally utilizing fewer parameters and enabling faster computation.  Additionally, the experiments observed findings that may be related to biological characteristics. This indicates that CNNs are still a strong competitor compared to Transformers and SSMs. We anticipate that this work will spark renewed interest in CNN-based methods for DNA foundation models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
Since various Transformer and SSM-based models are proposed in DNA language modeling, the authors conduct empirical studies of whether CNNs are truly being surpassed by these recently proposed approaches. With analysis results, this paper develops a simple yet well-designed CNN-based method called ConvNova, which identifies and proposes three effective designs: 1) dilated convolutions, 2) gated convolutions, and 3) a dual-branch framework for gating mechanisms. Through extensive empirical experiments, we demonstrate that ConvNova significantly outperforms recent methods on more than half of the tasks across several foundation model benchmarks.

### Strengths
* **(S1)** The paper addresses a critical problem in DNA embedding with a novel application of classical convolution, showing significant improvements in species-aware tasks.

* **(S2)** The overall presentation is well originated and easy to follow. It is clear that the authors provide step-by-step designs to improve the attention mechanism for better performance and efficiency.

### Weaknesses
 * **(W1)** Despite the efficient design, the proposed ConvNova is somewhat simple and lacks novelty and support. The (dilated) convolution with gating branch is not a new design (proposed by MogaNet [1] in 2022 and well studied by StarNet [2] and MambaOut [3] in 2024), especially after Mamba variants came out (i.e., the implicit long convolution with gating). The authors should discuss these background works (discussing in the related work section or comparing with them), and provide more supports of why the proposed design is specially useful in DNA applications (refer to Q1 for details).

* **(W2)** Although the authors have compared with several well-known DNA models, some recently published DNA models and pre-training works are overlooked (e.g., GPN [4], VQDNA [5], and DNABERT-S [6]). Meanwhile, there are various DNA benchmarks that should be referred to and compared (classical benchmarks like GUANinE v1.0 [7], BEND [8], and GUE [9]), especially some long-range benchmarks [10] where SSM-based models work well. From my perspective, I am still not sure or not convinced that the dilated convolution with gating aggregation could consistently outperform self-attention or SSM architectures.

### Questions
* **(Q1)** Is there any empirical analysis or theoretical support to verify that the dilated convolution is capable and more efficient than self-attention or SSM modules on the DNA tasks? For example, the authors could visualize the reception field or analysis the learned patterns to show that the dilated convolutions with gating learn better.

* **(Q2)** Some questions about the hyper-parameters in the network. How to determine the kernel size and the dilated ratio in ConvNova? Are there any implementation details of the ablation studies and providing the corresponding configurations (in addition to Table 9)? Meanwhile, is there more ablation of different designs (like analysis in [1, 2, 3]) of the gating branches as mentioned in Eq. (1) and Appendix A.3?

### Soundness
3

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
3

### Summary
The paper introduces a new convolutional-based DNA foundation model and shows that CNNs can be competitive with Transformers and SSMs both in terms of absolute performance as well as accuracy vs. speed tradeoffs

### Strengths
The paper presents strong, rigorous, and detailed results, with several strong baselines
The significance of the model itself is high, both for the application domain but what it means in the context of SSMs.
To me, DNA seems like the prime use case that SSMs, based on their performance profile, should be the winning model. A pure convolutional model outperforming Cadesus is a very important result in the context, and adds to the growing body of work that show SSMs and their complexities may not be necessary.

### Weaknesses
 - The paper needs to do a better job, in the main text, of demonstrating what specifically about the model is novel, and what specifically contributes to the superior performance of this model compared to prior CNN-based DNA models.

For example, is it just better pretraining data? Is it including the complement sequence? I saw dilations, and receptive field choice were shown to be a portion of this, and I saw the ablations on the different components.

However, the specific novelty of this design is a bit ambiguous to me. The figures need to be clearer to emphasize the novel components compared to prior CNN-based models. Specifically, just answering the question in explicit detail: CNNs have been around for a while, why didn't we find a high-performing model like this well before this? What new has been added that wasn't found before?

There should be some more qualitative analysis in the main text, mainly I would like to see an understanding of how the different model classes compare in the types of errors they make. For example, does the smaller receptive field contribute to certain types of errors for tasks where longer range reasoning is necessary?

### Questions
Also mentioned in the weaknesses section, CNNs have been around for a while, why didn't we find a high-performing model like this well before this? What new has been added that wasn't found before?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes to revisit CNN based architectures for DNA sequence modeling, and propose a new CNN based architecture, ConvNova. The authors show, with an extensive empirical study,  that the model has state of the art performance on several DNA modeling task when controlling for model size.

### Strengths
The authors have a high quality set of evaluation experiments for their method. This can be significant as it may lead to further research on CNN based architectures for sequence modeling. The writing is mostly clear and the author's proposal significantly improves the state of the art.

### Weaknesses
The novelty of the approach is somewhat limited, as CNNs have already been applied to this setting, and the training procedure is broadly the same as in the HyenaDNA paper.

The CNN architecture used is based on gated convolutions, which has already been proposed elsewhere, limiting the novelty.

To better understand the novelty of the approach, a benchmark comparing with a more standard CNN architecture would have been useful.

The paper seems to lack a clear motivation as to why this specific CNN architecture was proposed.

I would have expected to find a description of the pretraining data in the main paper.

I would say that calling the model a “foundation model” is somewhat misleading as the model used in the paper has 7M parameters and was pretrained for 14 hours on a single GPU.

### Questions
What is the pretraining dataset?

Did you benchmark the model against a more traditional CNN architecture?

Is the architecture inspired by the DNA task in some way?

### Soundness
3

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
2

### Summary
The paper argues that a well-designed convolutional neural network (CNN), when used as a DNA foundation model, can outperform Transformer- and SSM-based models not only in accuracy but also in inference speed, model size, and training cost. The authors introduce ConvNova, a model composed of dual-branched Gated Convolutional Blocks (GCBs). The GCBs incorporate dilated convolutions and avoid performance-degrading downsampling, as supported by empirical findings. Ablation studies demonstrate the benefits of the dilated convolutions, dual-branch architecture, and gated mechanisms within the GCBs. The proposed model achieves higher accuracy while maintaining a smaller parameter count compared to several state-of-the-art Transformer and SSM models.

### Strengths
The authors conducted a series of carefully controlled experiments using different random seeds to demonstrate the accuracy advantages of their design. They compared the proposed ConvNova model against state-of-the-art Transformer- and SSM-based models across various tasks, including two benchmarks for short-range input sequences (the Nucleotide Transformer Benchmark and the Genomic Benchmark) and two benchmarks for long-range tasks (the Bend Gene Finding and the Chromatin Profile Prediction). Overall, the experiments and the ablation study are robust and effectively support the claims and the effectiveness of the proposed design.

### Weaknesses
While the authors present solid empirical evidence, the paper lacks a clear discussion on the intuition behind the design, making it more like a technical report. For example, ConvNeXt [1] builds on a well-known variant, ResNeXt [2], and details the accuracy impact of each modification. In contrast, ConvNova does not seem to establish a clear rationale connecting it to previous CNN-based DNA foundation models, which makes the design choices appear somewhat ad hoc. Beyond demonstrating superior accuracy compared to Transformers and SSMs, it would be valuable to include an in-depth discussion and comparison with models like LegNet on block design, architecture, parameter count, and training schemes in the main text. The paper would benefit from a more thorough analysis of why the specific architectural choices, such as the dual-branch design and the use of dilated convolutions, lead to improved performance compared to existing CNN architectures for DNA sequence modeling. The lack of a clear connection to prior CNN-based models makes it difficult to understand the novelty and contribution of the proposed design beyond a specific hyperparameter configuration.

I found the organization of the paper somewhat confusing. For instance, the comparison of downsampling and dilation in Section 3.3 and Table 1 would be more appropriately placed in the experiments section. Additionally, given the variety of tasks with different state-of-the-art models and settings, I recommend adding a dedicated section that briefly outlines the experimental setup. This section should include the objectives of each task, descriptions of the baseline models, and the specific configurations used in each experiment. Furthermore, the paper lacks a clear explanation of how the receptive field of the dilated convolutions is determined and how this choice impacts the model's ability to capture long-range dependencies in DNA sequences. The absence of a detailed analysis of the receptive field makes it difficult to assess the model's suitability for tasks with varying dependency lengths.

### Questions
- What is the intuition and rationale behind using dilation over self-attention in a DNA foundation model? And why is dilation outperforming self-attention?
- How is the receptive field for the dilated convolutions determined?
- What factors contribute to the dual-branch design outperforming a single-branch approach?
- In addition to the details in Table 11 and Section A.4, could you provide a comparison between ConvNova and LegNet in terms of structure and training scheme, and explain why your design is superior?

### Soundness
3

### Presentation
2

### Contribution
2

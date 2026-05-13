# Benchmarking Predictive Coding Networks -- Made Simple

- Decision: Accept
- Scores: 8, 8, 6

## Abstract
In this work, we tackle the problems of efficiency and scalability for predictive coding networks in machine learning. To do so, we first propose a library called PCX, whose focus lies on performance and simplicity, and provides a user-friendly, deep-learning oriented interface. Second, we use PCX to implement a large set of benchmarks for the community to use for their experiments. As most works propose their own tasks and architectures, do not compare one against each other, and focus on small-scale tasks, a simple and fast open-source library adopted by the whole community would address all of these concerns. Third, we perform extensive benchmarks using multiple algorithms, setting new state-of-the-art results in multiple tasks and datasets, as well as highlighting limitations inherent to PC that should be addressed. Thanks to the efficiency of PCX, we are able to analyze larger architectures than commonly used, providing baselines to galvanize community efforts towards one of the main open problems in the field: scalability.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors undertake the very hard task of trying to streamline, standardise and robustify the scientific process in the subfield of Predictive Coding networks. They identify that the subfield suffers from a variety of issues such as poor comparisons between models, too simple baselines or benchmarks, and overall a lack of rigour in how potential proposed techniques are studied, compared, contrasted and analysed. This leads to the issue of making important issues hard to identify, and even harder to get a good critical mass of people working on them for resolution. 

The authors try to improve on this issues by offering: 

1.  A unified benchmark for predictive coding network models that is more expansive than others before it, utilising CIFAR100, Tiny ImageNet, FashionMNIST and MNIST. 
2. A library that allows quick and easy application of the benchmark on a target approach. 
3. A thorough evaluation of a number of key architectures and PC approaches on their benchmark, that can serve both a source of insights for the current state of the field and a good starting baseline for future approaches. 

Overall the proposal of the authors is an important and valuable one, and while the writing is OK, it is at times sloppy, with fluency and spelling mistakes, as well as inconsistent use of various terms. 

However overall a very good paper.

### Strengths
- Addresses Core Issues in PC Research: The paper tackles fundamental shortcomings in the subfield, such as inconsistent comparisons, overly simple benchmarks, and a lack of rigorous, standardized practices.

- Unified Benchmarking Framework: Introduces a comprehensive and standardized benchmark for PCN models, incorporating major datasets like CIFAR-100, Tiny ImageNet, FashionMNIST, and MNIST to ensure consistent and meaningful comparisons.

- Implementation of Open-Source Tool (PCX): Offers a JAX-based library that enhances research efficiency and accessibility, boasting up to 50x speed improvements via JIT compilation and seamless compatibility with modern ML tools.

- Thorough Experimental Evaluation: Conducts extensive tests on key PCN architectures and variants, backed by large-scale hyperparameter studies, establishing a solid baseline for future advancements.

- Deep Analysis of Training Mechanics: Provides valuable insights into energy propagation, initialization strategies, and stability across optimizers and architectures, which can guide targeted future research.

- Community-Centric Contribution: The open-source nature, complete with detailed documentation and tutorials, lowers the barrier to entry and encourages collaboration, setting a strong foundation for collective progress.

- Motivation for Future Research: Clearly identifies current limitations, such as scalability and energy flow issues, laying the groundwork for targeted solutions and deeper exploration.

- Competitive Performance on Benchmarks: Shows that PCNs can achieve performance on par with BP-trained models for small to medium-sized architectures, establishing a base for scaling up and further innovation.

Insightful 'weaknesses' highlighted by the paper that should not be perceived as a weakness of the paper itself imho.

Identification of Scalability Challenges: The paper highlights scalability issues inherent to PCNs but does not propose new solutions. While this reflects well on the depth of the analysis, it may be seen as a limitation in terms of contribution.
Performance Bottlenecks in PCNs: The analysis shows that while the proposed library offers performance improvements over prior implementations, it remains slower than backpropagation for more complex models. This insight underscores the current challenges facing PCNs but could be perceived as a weakness in terms of efficiency.
Sequential Processing Constraints: The authors identify that sequential layer updates are a significant bottleneck, impacting parallelism and efficiency. This is a critical finding for the field, though it might be seen as a shortcoming in practical use.
Theoretical Insight Depth: The paper provides an analysis of training mechanics, but it could go further in offering deep theoretical explanations for issues like energy propagation and training stability. This gap invites further exploration but could be seen as a weakness by readers looking for comprehensive theoretical coverage.
Implementation Constraints and Parallelization: The paper highlights that training time scales linearly with the number of layers due to current parallelization limitations. This insight is crucial for understanding the limitations of PCNs but might be perceived as a practical constraint in the work presented.

### Weaknesses
Weaknesses of the Paper:
- Writing and Terminology: The paper has inconsistencies in terminology and occasional grammar and spelling issues, along with unclear phrasing that affects readability and comprehension.
- Comparative Analysis Limitations: The paper could be strengthened by including more comparisons with other biologically inspired approaches and better situating its findings within the broader machine learning context.
- Practical Implications: The paper lacks a thorough exploration of how its findings translate to practical, real-world applications beyond academic benchmarks.
- Diversity of domains/tasks/modalities while a lot more than anything other out there for PC research, is still very limited compared to much more general benchmarks out there for general deep learning evaluation. Adding more domains, tasks and modalities would be very useful to having rigorous and insightful works done by people using it. 
- Architectures applied do not include any resnet, densenet or transformer architectures -- yes depth is an issue I understand, but using a shallow variant of any of these would be very useful.

### Questions
1. Why only JAX? Why not Pytorch? It seems like this goes against the spirit of the inclusiveness of your work. 
2. On Scalability Solutions: While the paper does an excellent job of identifying scalability issues in PCNs, do the authors have any preliminary ideas or suggestions for future work that could address these challenges?

3. Efficiency vs. Backpropagation: Given that the proposed PCX library is still slower than traditional backpropagation for complex models, are there any plans or ongoing work to bridge this efficiency gap?
3. Spelling, grammar and clarity points:

Here are the sections that could benefit from improved clarity, fluency, or grammar:

1. Line 110-111:
"different directions of research that either explored interesting properties of PC networks, such as their robustness and flexibility (Song et al., 2024; Alonso et al., 2022) , or proposed variations to"
- Extra space before comma after parenthesis
- Somewhat awkward phrasing

2. Lines 180-182: 
"In practice, we do not train on a single pair (x,y) but on a dataset split in mini-batches that are subsequently used to train the model parameters."
- Should be "split into mini-batches"

3. Line 229: 
"While interesting and important for the progress of the field,"
- Awkward start to sentence, could be rephrased for better flow

4. Line 270:
"We test the performance of PCNs on image generation tasks."
- Somewhat abrupt transition, could use better connection to previous section

5. Line 394:
"We observed a further link between the weight optimizer and the structure of a PCN that might hinder the scalability of PC"
- Run-on sentence that could be clearer if split or restructured

6. Line 443:
"PCX extensively relies on Just-In-Time compilation."
- Inconsistent capitalization of "Just-In-Time" compared to other instances of "just-in-time"

7. Line 469:
"In fact, in its current state, JIT is unable to parallelize the executions of the layers;"
- "executions" should be singular "execution"

8. Line 476:
"we have lied new foundations"
- Should be "laid new foundations"

9. Line 485:
"When this condition is released,"
- Should be "When this condition is relaxed," or "When this limitation is removed,"

10. Throughout the paper:
- Inconsistent spacing around mathematical symbols and equations
- Some inconsistent use of commas in complex sentences
- Occasional mixing of American and British English spellings

Figure 1: 

You want a figure to stand on its own without any context from the paper ideally. What is F here? Can we improve the clarity and informativeness of the caption and the figure itself?

These issues are relatively minor and don't significantly impact the paper's readability or scientific contribution, but addressing them would improve the overall polish of the manuscript.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper contributes a comprehensive library/framework that unifies the developing and testing for predictive coding networks (PCNs). Traditionally, the field suffers from lacking of unified metrics and open-source implementations, the contributed library well addresses the problem. Furthermore, with the contributed library, the paper is able to scale existing works onto larger datasets and achieves new SOTA on all the datasets. The paper also includes the popular algorithms in the field and benchmarked them extensively.

### Strengths
1. The benchmark results included in this work is very extensive which includes most of the popular baselines.
2. The design and usage of the contributed library are well documented with provided repos (I didn't run the code in this repo).
3. The analysis provided in the paper is well explained such as showing different results from different methods which makes the paper easy to read
4. With the contributed library, the paper is able to scale up the field to larger datasets which greatly improved the applicability of the methods in the field.
5. The work also shared some insights for sub-optimal cases of PCNs which can further guide the development of new methods.

### Weaknesses
1. Some figures can be improved, e.g. for figure 2, the method name can be draw above the images for better representation.
2. The main models used in the paper is MLP and VGG, since the library has been developed, we should probably test a few more model types such as resnet (shallow is OK if deep ones cannot be test) or vit. This could probably real more insights on the overall states of PCN algorithms.


### Questions
1. Can we test some models beyond VGG and MLP as mentioned in weakness? 
2. For the results in table 1, the result of VGG-5 is better VGG-7, does that mean PC works better when the number of layers is small. I think we need more data points here.
3. Also for table 1, can you include the same datasets for both VGG-5 and VGG-7, currently, the missing data points (CIFAR-10) makes it both hard to read the table and hard to make more in-depth comparison between these two cases.
4. I think it's better to provide the URLs at the beginning of the paper instead of at the end.

I will consider raising the scores if my questions can be addressed.

### Soundness
3

### Presentation
3

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
This paper addresses the trend in predictive coding networks (PCNs) literature of not comparing results against each other. To this end, the authors present a library that facilitates implementing and testing new PCNs, and they also propose several new benchmarks for evaluation. These benchmarks include larger networks and more complex tasks than those in previous works, and span discriminative as well as generative tasks. The paper evaluates several existing methods, including standard backpropagation, on these newly proposed benchmarks and analyzes the results.

### Strengths
### Originality
The main contribution of the paper is the PCX library which can be used to implement predictive coding networks, and the proposed benchmarks, which can be used to evaluate the scalability of new predictive coding networks.

### Quality 
The PCX library, owing to Just-In-Time compilation, is much faster than the baseline library. The reported performance (training times) of the PCX library shines against the baseline by Song et al.

### Clartity
The tutorials are of good quality. The Jupyter Notebook tutorials released with the paper are easy to set up and follow.

### Significance
The paper is well motivated.
1. Providing the community with the tools and benchmarks to compare their methods against others’ is a meaningful endeavour.
2. The benchmarks are designed to address scalability of PCNs.
3. The benchmarks are not limited to only discriminative tasks like classification, but also include generative tasks such as autoencoding and sampling from a learned joint distribution.

The following insights into PCNs were very interesting:
1. The AdamW optimizer performs poorly as the hidden layer size increases. This was also demonstrated well in the tutorial notebook.
2. Skip connections have a dramatic effect on the performance of PCNs.

The evaluation is extensive. A fair number of existing PCN methods were evaluated (standard PC, positive/negative/centered nudging PC, incremental PC, Monte Carlo PC).

### Weaknesses
I gave a score of 3 for Contribution but only 1 for Soundness. This is because I believe the PCX library is a valuable contribution to the community; however, I have reservations about some of the conclusions and claims made in the paper.

Consider the Energy propagation subsection of Section 5.1 (Energy and Stability). L377 says, “Note that the decay in performance as function of increasing γ is stronger for Adam despite being the overall better optimizer in our experiments. This suggests that possible directions for future improvements should aim at reducing the energy imbalance between layers.”. It is unclear to me how this conclusion that energy imbalance must be reduced was arrived at. I understand energy imbalance to be different from energy ratios in that the imbalance is minimized when the ratio is 1, i.e., both the layers have the same energy.
In Figure 5 (right), we see that the learning rate which minimizes the energy imbalances (i.e, make the ratio as close to 1 as possible) is 0.3. In Figure 5 (center right), we see that the performance of AdamW optimizer for a learning rate of 0.3 is much worse than 1e-3, 3e-3, and 1e-2, all of which have much higher energy imbalances. The same pattern can be observed in Figures 13 and 14. How do we conclude from this behaviour of AdamW that the energy imbalance must be minimzed? This also affects the claim in the abstract that the paper “clearly highlights what the current limitations of PCNs are”.

Next, in Section 4.1 (Discriminative Mode), L243 says that "The results show that the best performing algorithms, at least on the most complex tasks, are the ones where the target is nudged towards the real label, that are PN and NN.". The results for Discriminative mode are reported in Table 1. Assuming, based on L067, that complex tasks refer to CIFAR100 and Tiny ImageNet, I am unable to find data in the table that substantiates this claim. For VGG-5 models, centered nudging (CN) dominates both positive nudging (PN) and negative nudging (NN) for all the tasks except Tiny ImageNet (Top-1).
For VGG-7 models, all PC methods are beaten by either of the two variants of Back Propagation (BP-CE and BP-SE). Even considering only the PC methods, PN is consistently beaten by PC-CE, as is NN, with the exception of CIFAR-100 (Top-1).

Finally, in the Discussion subsection of Section 4.2 (Generative Mode), line 339 claims that “Thus, compared to artificial neural networks, PCNs are more flexible and require only half the parameters to achieve similar performance”. The fact that PCNs require only half as many parameters as an autoencoder neural network is evident because they can infer the hidden states of layers that have not been fixed (either to the input image for compression or to the compressed representation for generation). However, the paper demonstrates that this holds true only for small models, as the generative experiments were conducted exclusively on relatively small models (3 layers for autoencoding and generation via sampling, and 2 hidden layers for associative memory experiments). Conducting at least one experiment on a larger model, such as a VGG-7-scale model, could have strengthened this claim.

I am open to reconsidering my scores if these concerns are addressed.

The following is feedback and minor nitpicks about the presentation of the paper. Addressing these will improve the quality of the paper, but will not affect the scores.

1. The abbreviation “BP” is used in the paper without introducing it. The first reference to it is in the Appendix.
2. Figure 1 (b). Shouldn’t it be “hL is fixed to y”?
3. Table 3 can be made more intuitive to read by mentioning in the caption that it is a comparison of the two modes of associative memory tasks - Noise and Mask.
4. H and theta should be subscripts in L141
5. Citations are missing for several works (which, admittedly, a lot of us take for granted). Examples are CIFAR-10, MNIST, Fashion-MNIST, Tiny ImageNet, SGD, Adam, AdamW, VGG models.
6. Citations for each of the methods in the Algorithms subsection of Section 4 would make it easier for the readers to refer to the papers, even though they are all cited before.
7. Figure 5 would be better if it were indexed as Fig 5a to Fig 5d, instead of Fig 5 left, center-left, center-right and right.
8. The citation style in L239 is wrong.
9. L347 “How regularly the energy flows into the model”. Improve phrasing.
10. All references to Figure 5 right and center-right are inverted. See, e.g., L373 and L377.
11. Grammatical errors in a few places, such as L267, L355, L467

### Questions
Can you motivate the use of VGG-5 and VGG-7 models in the benchmarks? In terms of model sizes, they are roughly 3.8M and 4.5M, respectively, so they’re quite close to each other.

### Soundness
2

### Presentation
2

### Contribution
3

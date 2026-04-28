# Respect the model: Fine-grained and Robust Explanation with Sharing Ratio Decomposition

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
The truthfulness of existing explanation methods in authentically elucidating the underlying model's decision-making process has been questioned. Existing methods have deviated from faithfully representing the model, thus susceptible to adversarial attacks.
To address this, we propose a novel eXplainable AI (XAI) method called SRD (Sharing Ratio Decomposition), which sincerely reflects the model's inference process, resulting in significantly enhanced robustness in our explanations.
Different from the conventional emphasis on the neuronal level, we adopt a vector perspective to consider the intricate nonlinear interactions between filters.
We also introduce an interesting observation termed Activation-Pattern-Only Prediction (APOP), letting us emphasize the importance of inactive neurons and redefine relevance encapsulating all relevant information including both active and inactive neurons.
Our method, SRD, allows for the recursive decomposition of a Pointwise Feature Vector (PFV), providing a high-resolution Effective Receptive Field (ERF) at any layer.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors propose an explanation method for deep models called Sharing Ratio Decomposition (SRD) that pursues enhanced precision and robustness of its explanation. In extensive simulations, the method shows a strong and robust explanation performance across various kinds of metrics beyond the prior XAI methods. The main contribution of this work is to widen the view of XAI that should be pursued for achieving a reliable and robust explanation of deep model inference.

### Strengths
**Strength 1:** Explainable AI (XAI) is one of the most important research topics that directly tackle the explanation issue of the current deep learning models. Beyond the better explainability, the authors raise the multiple objectives that XAI should pursue, i.e., Localization, Complexity, Faithfulness, and Robustness, and argue that the proposed XAI, called Sharing Ratio Decomposition (SRD), is superior to the prior XAIs in the 'desiderata'. I am strongly convinced that the future XAI should consider an efficient, effective, precise, and robust explanation by pursuing the desired factors. The comprehensive experimental results in Table 2 clearly show the strength of the proposed XAI method, which is SRD.

**Strength 2:** A lot of qualitative results in the main paper and the supplementary truly help readers visually understand the benefits of SRD. These results clearly contrast SRD to the prior methods. I believe that efforts to show these qualitative results are very important to visually identify the explainability that often relies on the human-concept level evaluation of how well XAI explains the model's inference.

**Strength 3:** A bunch of prior works are clearly compared to the proposed XAI method via extensive simulation results (as shown in Table 2). I expect that the evaluation effort will promote extensive comparison with diversified viewpoints, i.e., Poi., Att., Spa., Fid., and Sta., in assessing future XAIs.

### Weaknesses
 **Weakness 1:** The '3. Method' part needs to be improved for better presentation. For readers who are a beginner in the XAI research field, I feel that a compact and clear description such as a pseudocode-style presentation or stepwise procedure explanation (e.g., 1. Feedforward an input, 2) Calculate PFV, 3) Decompose PFV, 4) Compute sharing ration through backward propagation, 5) Relevance is computed), would definitely help readers to understand the way that the method works. In this version of the article, the description is a quite verbal explanation.

**Weakness 2:** The key reasons behind the gains of SRD are not clearly analyzed. In this paper, the authors have separately pointed out the uniqueness of their method in multiple parts of the paper. However, I cannot fully understand the essential factors that make SRD be superior to other prior XAI methods. Is it due to the vector perspective, consideration of inactive neurons, decomposition of PFV, or any combinatorial effect of multiple factors?

### Questions
**Q1:** In the 'Weakness 1' issue, would you provide a stepwise description of the methodology?

**Q2:** In the 'Weakness 2' issue, would you clarify the main reason of the gains of SRD?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an XAI method called Sharing Ratio Decompostion at vector level. It can reflect the inference process at the vector level instead of neuron level. It also proposes a new observation method called APOP which can highlight the influence of the inactive neurons. The result on ImageNet dataset reach outstanding performance compared to SOTA.

### Strengths
1. The quantitative experiment result is good.
2. APOP is a novel observation method to highlight the influence of inactive neurons and easy to follow.
3. The deduction of SRD on forward and backward pass is rigorous.

### Weaknesses
1. Compared SOTA is limited and all methods were proposed before 2021. There are many CAM based methods in these two years.Why do not compare to the methods in these two years?
2. In equation 4, it mentions that the summation of modified sharing ratio is not 1. So will it cause some problem? It seems better to normalize ratio to 1 further.
3. The metrics used in experiment is quite different to other XAI methods. Is there any consideration in that?

### Questions
Questions can be seen in weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduce a novel interpretability method in this paper. Their approach differs from the past neural perspectives and starts from a vector perspective, leveraging gradient information and intermediate model output propagation computations. They attribute the input images based on the model’s inference process and explain the algorithm’s computation process from both forward and backward equivalent processes.

### Strengths
1.  The authors propose a new perspective with finer granularity, attributing based on vectors as units.
2.  The authors conducted experiments from aspects such as Localization, Complexity, Faithfulness, and Robustness based on previously proposed desiderata of interpretability, demonstrating the effectiveness of the algorithm.
3.  Additionally, the authors introduce an interesting observation worth further research, Activation-PatternOnly Prediction (APOP), indicating that retaining only the activation states in the network can still preserve the model’s inference capability to a certain extent.

### Weaknesses
1.  The experiments in this paper are all based on the ImageNet-S50 dataset, which only contains 752 samples. To better verify the effectiveness of the algorithm, it would be more persuasive to test on the ImageNet validation set like perturbation[1] and deletion & insertion[2] experiments do. The limited size of ImageNet-S50, and its focus on segmentation masks, raises concerns about the generalizability of the findings to more diverse datasets and tasks. The lack of testing on the full ImageNet validation set, which is a standard benchmark for image classification, makes it difficult to compare the proposed method with existing interpretability techniques under more realistic conditions.
2.  From my personal point of view, the APOP phenomenon is a very interesting and worthwhile topic for further research. However, I didn’t quite grasp how the APOP phenomenon helps with attribution in the model’s inference process. That is, this section doesn’t seem to be tightly connected with the paper’s main focus, the interpretability algorithm. The paper does not clearly articulate how the observation that activation patterns alone can preserve model performance relates to the proposed attribution method. The connection between the APOP finding and the core interpretability method is not well-established, making it unclear how this observation enhances the understanding of the model's decision-making process.
3.  The experiments in this paper are only based on VGG and ResNet backbones. Perhaps conducting experiments on backbones of different depths and comparing the algorithm’s performance on shallow layers and deep layers would make the paper more convincing. The absence of experiments on a wider range of architectures, including those with different connectivity patterns (e.g., DenseNets, Transformers), limits the scope of the evaluation. Analyzing the performance of the algorithm across different network depths and architectures is crucial to understand its robustness and general applicability.

### Questions
1. The paper's experiments should include testing on the larger ImageNet validation set for better verification.
2. The APOP, although interesting, doesn't seem connected to the motivation that focus on interpretability.
3. The paper should consider conducting experiments with different backbone architectures to strengthen its findings.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a novel eXplainable AI (XAI) method called SRD (Sharing Ratio Decomposition), which sincerely reflects the model’s inference process, resulting in significantly enhanced robustness in our explanations. Through experimental validation, this approach has yielded an intriguing result.

### Strengths
The writing structure is well-organized, the language is fluent, and it exhibits strong readability. The inclusion of rich visualizations and thorough experimental validation adds to its overall quality. In the scheme design, different from the conventional emphasis on the neuronal level, they adopt a vector perspective to consider the intricate nonlinear interactions between filters.

### Weaknesses
For the entire paper, the organization of the content is not very reasonable. There is limited coverage in the experimental description, whereas the related work section is extensive. The results in the experiments need more in-depth analysis and discussion.

All evaluations are performed on the ImageNet-S50 dataset, and it would be better to conduct evaluations on multiple datasets to better demonstrate the proposed method's generalization capabilities.

The experimental comparisons and performance improvements lack strong persuasiveness, and the conclusion section of the paper is lengthy and somewhat verbose.

### Questions
In the experiments, it is not clearly explained why the input resolutions vary between different methods. Furthermore, it's not clear how using different resolutions as inputs ensures the fairness of the experiments.

The existing methods have deviated from faithfully representing the model, making them susceptible to adversarial attacks. The author did not provide relevant discussions on this issue.

All the comparative methods used in the experiments are from 2014 to 2021, but it's not clear why more recent methods were not included.

The choice to target the Conv5_3 layer in VGG16 and the avgpool layer in ResNet50 is not adequately justified. Whether adjacent layers would have a significant impact is not addressed.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

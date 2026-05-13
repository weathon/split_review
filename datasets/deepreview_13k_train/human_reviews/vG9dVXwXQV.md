# Pre-Trained Vision-Language Model Selection and Reuse for Downstream Tasks

- Decision: Reject
- Scores: 5, 6, 8

## Abstract
Pre-trained Vision-Language Models (VLMs) are becoming increasingly popular across various visual tasks, and several open-sourced VLM variants have been released. However, selecting the best-performing pre-trained VLM for a specific downstream task is challenging since no single VLM can achieve promising performance on all downstream tasks, and evaluating all available VLMs is impossible due to time and data limitations. To address this problem, this paper proposes a novel paradigm to select and reuse VLM for downstream tasks, called Model Label Learning (MLL). The proposal contains three key modules: \emph{model labeling}, which assigns labels to each VLM to describe their specialty and utility; \emph{model selection}, which matches the requirements of the target task with model labels; and \emph{model reuse}, which applies selected VLMs to the target task in an ensemble manner. The proposal is highly computationally efficient and growable since the model labeling process is completed target task independent and the ability could grow with the number of candidate VLMs. We also introduce a new benchmark for evaluating VLM selection methods, including 49 VLMs and 17 target task datasets. Experimental results clearly demonstrate the effectiveness of the proposed method for selecting and reusing VLMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Selecting the best-performing pre-trained Vision-Language Models (VLMs) for a specific downstream task is challenging since no single VLM can achieve promising performance on all downstream tasks, and evaluating all available VLMs is impossible due to time and data limitations. 
To address this problem, this paper proposes a novel paradigm to select and reuse VLM for downstream tasks, called Model Label Learning (MLL). 
The proposal contains three key modules: model labeling, which assigns labels to each VLM to describe their specialty and utility; model selection, which matches the requirements of the target task with model labels; and model reuse, which applies selected VLMs to the target task in an ensemble manner. 
The proposal is highly computationally efficient and growable since the model labeling process is completed target task independent and the ability could grow with the number of candidate VLMs.

### Strengths
- The proposed method is easy to understand.

### Weaknesses
 - The novelty of the proposed method is weak. The main contribution of this paper is the model selection when ensembling multiple VLMs. However, there is no discussion or experimental analysis of the selected models during this process. What models are selected will give the readers a hint about the proposed method's characteristics or advantages.
- The analysis in this paper is too simple. After the model selection, what models are selected? As the main contribution is the model selection, the authors should show the selected models to understand the proposed method's characteristics and advantages.
- As a design choice analysis, the authors only tried K values to be 1 and 3. Although finding the best hyper-parameter is essential, why didn’t the authors try other values for K? The number of selecting models K is more important than the size of the model hub.
- Other essential design choice analyses are also missing. For example, in Eqn 8, why did the authors give high loss weight to models with high entropy? Is it the best choice of the weight values? Also, in Eqn 7, how is the hyper-parameter alpha decided, and how does it affect the model's performance?
- More importantly, the comparison with recent models is missing. There are several ways to improve VLMs without training, at least with the improved prompt-based approaches [1,2]. The authors should show the advantages of ensembling the models instead of the existing ways of improving VLMs. Also, ensembling models increases the number of total parameters. The authors should analyze the efficiency of the model ensemble compared to the existing approaches.

### Questions
Please refer to the questions in the weakness.

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper introduces Model Label Learning (MLL), a new approach for selecting and repurposing Vision-Language Models (VLMs) for downstream tasks. It comprises three main components: model labeling to categorize VLMs by their expertise, model selection to align VLMs with task requirements, and model reuse to integrate chosen VLMs into an ensemble for task application.

### Strengths
**[New perspective]** This work focuses on the selection and reuse of pre-trained VLMs to better suit the need of specific downstream tasks, which is novel and practical.

**[Good presentation]** This paper is well-written, making it easy to follow.

**[Thorough evaluation]** Extensive experiments have been done to evaluate the effectiveness of the proposed strategy.

### Weaknesses
 **[Need more explanation]** 
- In Figure 1, the details of the evaluated VLMs are missed. Please add this information in the caption for better understanding.
- The paper missed the introduction of ImageNet Baseline (INB). Is the best-performing model on ImageNet, i.e., EVA02-E-14?

**[Could be improved]** 
- In line 245, this work randomly selects images $X_v$ from sample datasets to serve as representations for each node. Is there a more elegant solution for this, e.g., using the mean of several samples from the same class?
- For model reuse, the work selects top-k models with a simple ensemble approach. It would be nice to discuss or compare more advanced ensemble approaches in VLMs, e.g., “Beyond Sole Strength: Customized Ensembles for Generalized Vision-Language Models, ICML 2024”.

**[Experiments]** 
- In Table 1, both INB and ModelGPT use the best-performing single model alone for evaluation. It would be nice to leverage them to select more models with ensemble for prediction when comparing the proposed method with 3-model ensemble. For example, the authors can select top-3 models on ImageNet for INB and do similar things for ModelGPT. Including this comparison can enhance the understanding of the effectiveness of the proposed method.
- Since the proposed MLL introduces three procedures, each costing extra time, could the authors provide the additional time introduced? This could offer insights on the trade-off between performance and time.

### Questions
Please refer to the weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper explores a practical VLM reuse problem and proposes Model Label Learning (MLL), which efficiently selects and reuses pre-trained Vision-Language Models (VLMs) for downstream tasks. The framework consists of three modules: model labeling, which assigns labels to VLMs based on their capabilities; model selection, which matches these labels to task requirements; and model reuse, which employs an ensemble of selected models. In addition, a large-scale benchmark, including 49 VLMs and 17 datasets, is introduced to evaluate MLL’s effectiveness, with experimental results showing promising scalability and effectiveness.

### Strengths
1. The problem explored in this work is practical and meaningful. The proposed MLL framework provides an efficient way to select and reuse VLMs by leveraging a semantic graph and task-specific labels.

2. The method demonstrates good scalability. The use of a semantic graph allows MLL to expand as new models or tasks are added, making it adaptable to diverse visual tasks.

3. The paper is well-organized and easy to follow.

### Weaknesses
1. Regarding the scalability of the constructed semantic graph, if new nodes are added to the graph, is it necessary to add images to the sampled dataset to represent these new nodes? Additionally, have the authors considered using different datasets as the sampled dataset? If so, would different datasets impact the final performance? Specifically, the impact of using a dataset with significantly different image characteristics (e.g., medical images or satellite imagery) compared to ImageNet should be explored, as this could reveal limitations in the model's ability to generalize across diverse visual domains. The current reliance on ImageNet might bias the model labeling process, potentially leading to suboptimal performance on tasks with different visual characteristics.

2. For each target dataset, the highest performance achieved by any model in the model hub should also be included as a baseline result. This would help evaluate the effectiveness of the proposed method in selecting models. Without this baseline, it is difficult to assess whether the proposed method is truly selecting the best models or simply achieving comparable performance to the best individual model.

3. As K is a core hyperparameter, more experiments analyzing its impact should be included, as the paper currently only presents results for K=1 and K=3. A more comprehensive analysis of K, including performance and computational cost at various values, is suggested. The paper should also investigate the sensitivity of the model to different values of K, and provide guidance on how to choose the optimal K for different tasks. The current analysis is insufficient to understand the trade-offs between performance and computational cost when varying K.

### Questions
In addition to the points listed in weakness, the VLMs in the current model hub are primarily designed for image classification tasks. Have the authors considered expanding the proposed pipeline to accommodate more complex tasks, such as segmentation?

### Soundness
3

### Presentation
3

### Contribution
3

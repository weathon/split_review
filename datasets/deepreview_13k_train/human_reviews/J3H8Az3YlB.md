# RECAST: Reparameterized, Compact weight Adaptation for Sequential Tasks

- Decision: Accept
- Scores: 5, 6, 6, 6

## Abstract
Incremental learning aims to adapt to new sets of categories over time with minimal computational overhead.  Prior work often addresses this task by training efficient task-specific adapters that modify frozen layer weights or features to capture relevant information without affecting predictions on any previously learned categories.  While these adapters are generally more efficient than finetuning the entire network, they still can require tens or hundreds of thousands of task-specific trainable parameters even for relatively small networks, making it challenging to operate on resource-constrained environments with high communication costs like edge devices or mobile phones.
Thus, we propose \textbf{Re}parameterized, \textbf{C}ompact weight \textbf{A}daptation for \textbf{S}equential \textbf{T}asks (\textbf{\methodabbrev}), a novel method that dramatically reduces the number of task-specific trainable parameters to fewer than 50 – several orders of magnitude less than competing methods like LoRA.
\methodabbrev{} accomplishes this efficiency by learning to decompose layer weights into a soft parameter-sharing framework consisting of a set of shared weight templates and very few module-specific scaling factor coefficients. This soft parameter-sharing framework allows for effective task-wise reparameterization by tuning only these coefficients while keeping the templates frozen. 
A key innovation of RECAST is the novel weight reconstruction pipeline called Neural Mimicry, which eliminates the need for training in our framework from scratch.  %The pipeline allows for high-fidelity emulation of existing pretrained weights within our framework and provides quick adaptability to any model scale and architecture. 
Extensive experiments across six diverse datasets 
demonstrate \methodabbrev{} outperforms the state-of-the-art by up to $3\%$ across various scales, architectures, and parameter spaces. 
Moreover, we show that RECAST's architecture-agnostic nature allows for seamless integration with existing methods, further boosting performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a Neural Mimicry method to study a very small set of parameters for continual learning purposes. It studies both ViT and ResNet applications. It showed performance benefits over several benchmarks.

### Strengths
- The paper studies an important task.
- Motivating towards neural mimic and learnings from proxy domains are helpful in solving the CL tasks.

### Weaknesses
 - Experiments are very small scale. Two target models are only ~21M in size (Ln 305), and does not demonstrate scalability to large models.
- No forgetting values are presented that are critical aspects of CL learning setups.
- Fig. 1 is misleading and hard to get the 2*10^-6 parameters - instead this is a ratio instead of parameters. Moreover, it's not thoroughly shown this is a parameter that scales across networks. Would it be the same for LLM? Otherwise stating the method yields <<<1% can be fairly misleading, and in fact wrong if the units are parameters.

### Questions
As above.

### Soundness
2

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
3

### Summary
This paper addresses the problem of continual learning with the goal of creating a learning pipeline that reduces the number of learnable parameters, making it feasible for resource-limited devices. To achieve this, the authors propose a Neural Mimicry pipeline, which decomposes model weights into a bank of templates. Using these frozen templates, the model only learns coefficients for subsequent downstream tasks. Experimental results highlight the potential of the proposed method. However, I have several questions, and my detailed comments are as follows.

### Strengths
The proposed idea of incorporating Neural Mimicry into continual learning is novel and interesting. By decomposing model weights into frozen template banks and focusing solely on learning coefficients, the approach significantly reduces the number of learnable parameters. This paper introduces a new pipeline and valuable insights for the continual learning community.

Experiments on both CNN and ViT-small models demonstrate the effectiveness of the proposed method and highlight its architecture-agnostic nature.

### Weaknesses
The writing in this paper could be improved. For the pseudo-code, it would enhance readability to introduce the notations alongside the code for easier understanding. Additionally, more details on how to obtain the pre-trained model weights should be clearly provided.

The effectiveness of the method on larger models and datasets has not yet been adequately addressed.

In Table 1, why the total storage for RECAST + Piggyback/CLR increase linearly? For CNN-based models, why can’t this be further reduced, given that the learnable task parameters are already minimized from  $P$  to  $4 \times 10^{-3} P$ ?

In Table 2, why does the total storage remain unchanged? As more tasks are added, shouldn’t total storage also increase with  $M + T \times 6/8 \times 10^{-4} Pr$ ?

Efficiency in training/learning on edge devices is also important. It would be highly valuable to include a comparison of wall-clock training time and GPU memory in Tables 1 and 2. Given the significantly reduced number of learnable parameters, the proposed method should enhance training efficiency, which could be seen as an advantage of this approach, but empirical evidence is needed to confirm this.

It would also be helpful to report the training complexity of the Neural Mimicry process.

Finally, in Table 1, why do the accuracies for EWC, LWF, and GDUMB perform so much worse than ResNet-34?

### Questions
How are the pre-trained weights obtained for further Neural Mimicry decomposition? This seems quite important for the algorithm’s performance. If the model is pre-trained on data that differs significantly from the sequential tasks that follow, learning only coefficients may be insufficient, in my view.

In Table 1, why the total storage for RECAST + Piggyback/CLR increase linearly? For CNN-based models, why can’t this be further reduced, given that the learnable task parameters are already minimized from  $P$  to  $4 \times 10^{-3} P$ ?

How does the algorithm perform with larger models and datasets, such as ViT-base/Large with the ImageNet dataset? Would the Neural Mimicry method still be effective? Further discussion on this would be beneficial.

In Table 2, why does the total storage remain unchanged? As more tasks are added, shouldn’t total storage also increase with  $M + T \times 6/8 \times 10^{-4} Pr$ ?

Efficiency in training/learning on edge devices is also important. It would be highly valuable to include a comparison of wall-clock training time and GPU memory in Tables 1 and 2. Given the significantly reduced number of learnable parameters, the proposed method should enhance training efficiency, which could be seen as an advantage of this approach, but empirical evidence is needed to confirm this.

It would also be helpful to report the training complexity of the Neural Mimicry process.

Finally, in Table 1, why do the accuracies for EWC, LWF, and GDUMB perform so much worse than ResNet-34?

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
4

### Summary
In this work, the authors propose a parameter efficient task incremental learning method. Specifically, the proposed method reparameterizes the original model by using pre-trained template banks and lightweight learnable coefficients for each tasks during incremental learning. In the experimental results, the proposed method shows better accuracy with less trainable parameters when combining with previous incremental learning methods.

### Strengths
1. The proposed method can reduce learnable parameter for incremental learning.

2. In the experiments, the proposed methods shows better accuracy with less trainable parameters when combining with previous incremental learning methods.

### Weaknesses
1. The paper is not well written and not well organized. For example:
    
    (1) The proposed method and related works are mixed together in Section 2.
    
    (2) Subsection 2.1 introduces too many concepts from later sections, making it difficult to follow.
   
    (3) The opening paragraphs of Subsections 2.1 and 2.2 are largely redundant.

     (4) The overview of the proposed RECAST method (Fig. 2) should be introduced at the beginning of Section 2, but it isn’t presented until Subsection 2.2.

2. The proposed RECAST method itself does not seem directly related to task incremental learning.

3. The paper lacks sufficient background information, especially on relevant works like Template Mixing methods, making it difficult to assess the novelty of the approach.

4. It is unclear how RECAST integrates with previous incremental learning methods, as shown in Tables 1 and 2.

### Questions
Overall, this work appears to introduce a new parameter-efficient task incremental learning method, which significantly reduces the number of learnable parameters while improving accuracy when combined with previous incremental learning techniques. However, the current version has presentation quality issues, and the contribution of the technical aspects remains unclear. My specific questions are as follows:

1. What are the technical differences between the proposed RECAST and previous Template Mixing methods? For example:
   - How does the design of template banks and coefficients differ in RECAST?
   - How does RECAST support incremental learning with substantially fewer learnable parameters, whereas Template Mixing methods do not achieve this?

   It's essential to clarify the specific differences to highlight the novelty of the proposed method.

2. How does RECAST balance model plasticity and stability in incremental learning? From my understanding, RECAST reparameterizes the model using lightweight coefficients and frozen template banks for each downstream task, making it a parameter-efficient fine-tuning method rather than one specifically designed for incremental learning. In the experiments, RECAST is combined with existing incremental learning methods to achieve better performance. If this understanding is correct, it would be useful to compare RECAST with other parameter-efficient fine-tuning methods, such as prompt-tuning, LoRA, and DoRA.

3. How does RECAST integrate into existing incremental learning methods, as shown in Tables 1 and 2?

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
RECAST is a Task Incremental Learning (TIL) method that efficiently reparameterizes model components to emulate a pretrained target network by decomposing weights into shared templates and module-specific coefficients. The shared templates, stored in a template bank, match the shape of each layer and remain fixed across tasks, while the module-specific coefficients are fine-tuned for each new task. 

Through a process called Neural Mimicry, RECAST selects a target model and combines the templates and coefficients to approximate it. The approach is architecture-agnostic and requires minimal parameter updates across tasks.

### Strengths
- Clear presentation of results, focusing on both parameter efficiency and storage alongside accuracy. 
- The method enhances existing adapter-based methods, making it compatible and valuable as a supplementary tool. 
- It is versatile across architectures, with applicability to both CNNs and Transformers. 
- The setting is flexible, allowing adjustment of groups *G* and templates *n* to achieve the desired level of model compression.

### Weaknesses
I recommend adding another baseline based on rehearsal, such as ER[1], ER-ACE[2], or DER++[3]. While the proposed method is more aligned with adapter-based approaches, claiming strong performance in settings utilizing a memory buffer without including one of these established baselines for comparison seems somewhat unfair.

I understand that the accuracy reported is averaged across the six datasets used at the end of training. However, I'm curious if accuracy varies between tasks encountered earlier in training and those seen later. Including a table that shows accuracy results for individual tasks would strengthen the paper’s validity. This would also relate to Question 1 regarding the influence of task order.


    [1] Jeffrey S Vitter. Random sampling with a reservoir. ACM Transactions on Mathematical Software (TOMS), 11(1):37–57, 1985 
    [2] Lucas Caccia, Rahaf Aljundi, Nader Asadi, Tinne Tuytelaars, Joelle Pineau, and Eugene Belilovsky. New Insights on Reducing Abrupt Representation Change in Online Continual Learning. In International Conference on Learning Representations Workshop, 2022. 
    [3] Pietro Buzzega, Matteo Boschini, Angelo Porrello, Davide Abati, and Simone Calderara. Dark Experience for General Continual Learning: a Strong, Simple Baseline. In Advances in Neural Information Processing Systems, 2020.





**About LoRA and Figure 3**

2. It’s not entirely clear what is being evaluated in Figure 3. 
While a comparison with LoRA is certainly necessary in this work, could you clarify what "CF" stands for in the figure?

3. Additionally, rather than comparing to LoRA-only, it might be more informative to use the same baseline using LoRA in one case and RECAST in the other, e.g., fine-tuning the same backbone with the two methods.
It’s possible that Figure 3 already presents this setup, as it seems ViT-Small is used as the backbone and lower bound. If this is indeed the case, the figure caption and related section would benefit from clarification, with additional emphasis on these details to enhance interpretability.

4.  Furthermore, the comparison does not appear to fully explore the parameter range for both methods; although the x-axis in the plot represents the number of parameters, the methods are not evaluated across the entire range, and a comparison with the same number of parameters is only partially explored. Could you clarify the reasoning behind this?

**CL Setting**
5. Is there a specific reason why the authors have chosen to focus exclusively on the Task Incremental Setting, rather than exploring the more challenging Class Incremental Setting?

### Questions
1.  Does the task order adhere to the sequence in which the datasets are presented in the text (lines 294-296), or does averaging across three different runs involve altering the task order?  
I believe exploring the latter could be an intriguing study on how task order impacts weight adaptation and whether the learned coefficients are affected by such variations.  

**About LoRA and Figure 3**

2. It’s not entirely clear what is being evaluated in Figure 3. 
While a comparison with LoRA is certainly necessary in this work, could you clarify what "CF" stands for in the figure? 

3. Additionally, rather than comparing to LoRA-only, it might be more informative to use the same baseline using LoRA in one case and RECAST in the other, e.g., fine-tuning the same backbone with the two methods.
It’s possible that Figure 3 already presents this setup, as it seems ViT-Small is used as the backbone and lower bound. If this is indeed the case, the figure caption and related section would benefit from clarification, with additional emphasis on these details to enhance interpretability.

4.  Furthermore, the comparison does not appear to fully explore the parameter range for both methods; although the x-axis in the plot represents the number of parameters, the methods are not evaluated across the entire range, and a comparison with the same number of parameters is only partially explored. Could you clarify the reasoning behind this?

**CL Setting**
5. Is there a specific reason why the authors have chosen to focus exclusively on the Task Incremental Setting, rather than exploring the more challenging Class Incremental Setting?

### Soundness
2

### Presentation
2

### Contribution
3

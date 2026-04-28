# Solving Continual Offline RL through Selective Weights Activation on Aligned Spaces

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 3, 8, 3

## Abstract
Continual offline reinforcement learning (CORL) has shown impressive ability in diffusion-based lifelong learning systems by modeling the joint distributions of trajectories.  
However, most research only focuses on limited continual task settings where the tasks have the same observation and action space, which deviates from the realistic demands of training agents in various environments.
In view of this, we propose Vector-Quantized Continual Diffuser, named \ourmodel{}, to break the barrier of different spaces between various tasks.
Specifically, our method contains two complementary sections, where the quantization spaces alignment provides a unified basis for the selective weights activation.
In the quantized spaces alignment, we leverage vector quantization to align the different state and action spaces of various tasks, facilitating continual training in the same space.
Then, we propose to leverage a unified diffusion model attached by the inverse dynamic model to master all tasks by selectively activating different weights according to the task-related sparse masks.
Finally, we conduct extensive experiments on 15 continual learning (CL) tasks, including conventional CL task settings (identical state and action spaces) and general CL task settings (various state and action spaces).
Compared with 16 baselines, our method reaches the SOTA performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a method for the problem of continual offline reinforcement learning. The proposed method combines two modules: the Quantized Spaces Alignment (QSA) module, which standardizes different state and action spaces by using vector quantization to map them into a unified representation, and the Selective Weights Activation (SWA) module, which preserves knowledge from prior tasks by activating only relevant model weights for each new task through a masking mechanism. Extensive experiments show that the proposed method consistently outperforms existing methods, validating the effectiveness of this proposed method.

### Strengths
- Overall this paper contains a lot of new ideas. Using a VQ-VAE model to encode different tasks seems to be a reasonable way to enable the generalization of diffusion-based RL methods. 

- The idea of selecting activation weights in a U-Net diffusion model effectively addresses catastrophic forgetting by isolating task-specific weights. 

- The authors provided pretty comprehensive evaluation to demonstrate the effectiveness of this work both qualitatively and quantitatively.

### Weaknesses
 - The proposed method is a little bit complicated and might require significant computational resources and engineering efforts. Specifically, the combination of VQ-VAE for state and action space quantization, a diffusion model for policy learning, and a task-specific masking mechanism introduces several layers of complexity. The training process, involving multiple stages and components, could be computationally expensive and require careful hyperparameter tuning, potentially limiting its accessibility to researchers with limited resources.

- This method is designed for task-aware settings with explicit task boundaries, which could reduce its applicability in task-free continual learning scenarios where such boundaries are not predefined. The reliance on explicit task identifiers for mask selection and weight activation makes it unsuitable for environments where task transitions are not clearly demarcated or are unknown a priori. This limits the method's applicability in more realistic continual learning scenarios where task boundaries are not always available.

- It seems that the propose method, through effective, is a combination of existing learning methods, e.g. VQ-VAE, Diffusion, tasks masks. While the integration of these components is novel, the core techniques are not fundamentally new. The use of VQ-VAE for space discretization, diffusion models for policy generation, and masking for knowledge preservation are all established techniques, and the paper does not clearly demonstrate a significant departure from these existing methods.

### Questions
- Can the learned masks be visualized? Visualizing the masks could reveal task similarities and therefore can provide important insight for this proposed method. 
- Can this method detect non-periodic task changes?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper propose Vector-Quantized Continual Diffuser (VQ-CD) for any offline continual reinforcement learning tasks, including the tasks with different observation and action space. Specifically, quantized spaces alignment (QSA) module aligns different state and action spaces (with even different dimensions) to perform continual learning within the same space. Selective weights activation diffuser (SWA) module preserves the previous knowledge by separating task-related parameters with task-related masking. VQ-CD achieves SOTA performance on 15 continual tasks comparing with 16 baselines.

### Strengths
1. Traditional continual reinforcement learning approaches are significantly limited as they only consider tasks with consistent state and action spaces. This paper successfully addresses the challenge of tasks with diverse state and action spaces through the innovative use of a quantized spaces alignment module. 
2. The baselines compared in the paper are thorough and comprehensive, and the experimental environments considered are sufficiently diverse. These aspects robustly demonstrate the superiority of VQ-CD.

### Weaknesses
The paper appears to lack a significant amount of crucial details, which hinders my understanding of the algorithms presented. 
1. The paper does not clarify how the 'return' is utilized. Based on Section 3.2, I guess that the algorithm employs the 'return' as a condition. So, is it the 'return' or the Q-function that is being used? Additionally, how is the target return or target function determined during the inference phase? 
2. Within the QSA module, which parameters are shared, and which need to be retrained for different tasks?

### Questions
1. What is the "diffusion-based lifelong learning systems" in Abstract?
2. Figure 1 appears somewhat cluttered and hard to understand. Labeling the sequence within the figure would enhance its clarity.

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work proposes a novel method for continual offline reinforcement learning called VQ-CD that combines vector quantization with diffusion for continual learning.
The vector quantization part enables training of a unified state and action space such that VQ-CD  can be trained jointly on environments that provide different state/action spaces.
The policy is based on a diffusion model and weight masking that relies on task information.
The weight masks are constructed in a manner that they can be readily merged into a single model after training.
VQ-CD exhibits strong performance on Ant-dir, CW10, and D4RL environments with different state/action spaces compared to baselines.

### Strengths
The idea of leveraging vector quantization to learn a unified state/action space is strong and enables joint training on spaces of different dimensionality.

Empirical evidence seems strong and the method is compared against plenty of baselines.

Ablation studies highlight the importance of combining VQ with CD.

### Weaknesses
 **Significance of results:**

While I appreciate the number of experiments conducted and baselines the authors trained, I am not entirely certain the compared methods are state of the art. One particular baseline that comes to mind is L2M [1], which constructs unified state and action spaces  (similar to what QSA does) and incorporates a task matching mechanism to train separate weights for each task (similar to SWA). Therefore, L2M should be added as a baseline. Moreover, the unified state/action space of L2M can be used as an additional ablation study to the VQ approach, as it is simpler and does not require training.


**Limitations:**

The authors do not elaborate on limitations, however there are notable ones that should be mentioned:
- Training needs to be conducted on each task separately, resulting in separate model checkpoints with different masked weights, this scales linearly with the number of tasks
- VQ-CD relies on task information, other methods [1] can be used in a task-agnostic manner

**Presentation:**

First, the title overclaims the contribution of the paper as it does not "solve" the field, please consider renaming. Please also rephrase "any CL tas sequence settings", to something like "CL with different state/action spaces", as "any CL task" is ill-defined. Figure 1 only shows the VQ-CD training pipeline, but line 465 talks about "return-based action generation" which is never explained in the methodology. In fact, it is never explained whether the diffusion part constitutes the policy and how the inverse dynamics model is actually used. Can the authors elaborate in more detail about what is the policy and how the inverse dynamics model is used? Figure 2 is never referred to in the text. Can the authors adjust Figure 4 so that the task boundaries are visible? As of now it is not clear at which steps the task is switched as there are now clear differences in the learning curves. Line 423 sounds like state and action padding is being used for VQ-CD, but I assume it is only used for baselines, is this correct? Line 526 sounds like one action vector is being decomposed into several latent vectors, however VQ only quantizes into a single latent. It is not clear what the labels in Figure 7 indicate, can the authors elaborate and make it more explicit?

### Questions
- $w$ in line 193 has not been defined, what is it?
- Is there any intuition about why the constraint in eq. (2) is important?
- The constraint in eq. (2) could easily be incorporated in the loss function, why is clipping used?
- What are "nonsignificant masks" (line 352)
- What is the source of the data for CW10 and MuJoCo Ant-dir?
- How is it possible that VQ-CD is better than Multitask on two of the D4RL tasks?
- Why would the gaussian constraint for VAE hurt space alignment?
- How does reconstruction look for VAE-CD in Table 2? Only VQ-CD and AE-CD are shown there.
- Why does multitask baseline performance decrease with VQ state/action spaces (Figure 11)?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes a composite method to perform continual offline reinforcement learning by means of denoising diffusion probabilistic models (DDPMs). Each CORL task can have different observation and action spaces, which are aligned through a mechanism termed quantized space alignment (QSA). Continual learning performance is ensured by using a masking strategy (selective weights activation, SWA) that assigns distinct weights in the DDPM to distinct tasks. The paper presents an experimental evaluation on various  established continual RL benchmarks that show that the proposed method performs better than SOTA, as well as an ablation and parameter importance study to identify relevant parameters.

### Strengths
The paper presents an interesting approach to continual RL using DDPMs, a rarely used technique that has great merit. In general, modeling of policies by generative models is a very attractive idea. Experimental verification uses established benchmarks and compares to established SOTA methods, producing good results. The ablation study and the parameter importance investigation are interesting as well. The idea of aligning perceptual and action spaces in a common representation is worthy of attention.

### Weaknesses
 It is really hard to understand the big picture of the article. Figure 1 is not really helping since it does not indicate data flow through the model. It is only by studying the algorithm in the appendix that I could understand what the various components actually do, in which order. That algorithm should be moved to the main text, or els Fig.1 should be improved and simplified.
        
 This is not really continual learning, as you are processing all data in one go in Alg.1 during the QSA pretraining step. In a CL setting, you would have access to data from task i only when training on task i, but not before. So, from a CL perspective, adapting QSA in one go prior to real RL training is cheating because you are looking into the future.
    
 In the same vein: *if* you have access to all collected data, why use CL at all and not train everything at once?
    
 It is not clear how this method could scale to more tasks when the mask is filled. It would be very helpful to comment on this, and why you do not simply train a separate DDPM for each task.    
        
 Important details are simply missing: 1) how do you use a diffusion model and the inverse dynamics model to generate actions? What role does $\psi$ play? What are the dimensions of obs and action spaces for the different tasks? How do you apply DDPMs to data that are not images (e.g., actions)?
    
 It is unclear how the SOTA methods are implemented, I can find no information at all except the references. What parameter settings? What libraries? Without this information, comparing to SOTA is meaningless since nothing can be reproduced.
    
It is not made clear what the benefit is of having a single RL controller learn policies for tasks with different state/action spaces. The paper would benefit from examples here.
        
The language of the paper is often imprecise or slightly incorrect, please be sure to fix this.

More comments:
3.2 the notion of "state sequences" and is unclear, and this paragraph is hard to understand. Maybe explain this in more detail. what is $\tau_s^{0:K}$ ?
3.2 Same goes for the notion of "inverse dyanmics model": what is this for? It is never mentioned again...
3.2 " tailored state sequences to facilitate training", what does this mean? Unclear...
General: very few details given for DDPM usage: input space, action space, ...
General: Continual offline reinforcement learning requires a more in-depth introduction and justification, as offline and reinforcemenet learning seem to be contradictory concepts. What is the advantage here? What can ORL do that RL cannot, and vice versa?

### Questions
- For evaluation: is it necessary to know what task you are currently performing evaluation for?
- If no: how do you select the right mask at test time?

### Soundness
3

### Presentation
1

### Contribution
1

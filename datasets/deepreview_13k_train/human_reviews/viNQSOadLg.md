# Biological Sequence Editing with Generative Flow Networks

- Decision: Reject
- Scores: 5, 6, 6

## Abstract
Editing biological sequences has extensive applications in synthetic biology and medicine, such as designing regulatory elements for nucleic-acid therapeutics and treating genetic disorders. The primary objective in biological-sequence editing is to determine the optimal modifications to a sequence which augment certain biological properties while adhering to a minimal number of alterations to ensure safety and predictability. In this paper, we propose GFNSeqEditor, a novel biological-sequence editing algorithm which builds on the recently proposed area of generative flow networks (GFlowNets). Our proposed GFNSeqEditor identifies elements within a starting seed sequence that may compromise a desired biological property. Then, using a learned stochastic policy, the algorithm makes edits at these identified locations, offering diverse modifications for each sequence in order to enhance the desired property. Notably, GFNSeqEditor prioritizes edits with a higher likelihood of substantially improving the desired property. Furthermore, the number of edits can be regulated through specific hyperparameters. We conducted extensive experiments on a range of real-world datasets and biological applications, and our results underscore the superior performance of our proposed algorithm compared to existing state-of-the-art sequence editing methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
* In this paper, the authors present a novel sequence editing method that leverages GFlowNet. This method relies on a pre-trained flow function to evaluate the potential for substantial property improvement within a given sequence. Furthermore, it generates a variety of edits using a stochastic policy. 
* The properties of the edited sequences are analyzed by assessing the lower and upper bounds of the reward function. 
* To evaluate the effectiveness of this approach, the authors conducted real data experiments and compared their method to three baseline approaches. They assessed performance using various metrics, including property enhancement, edit percentage, and diversity in TF binding.

### Strengths
The experimental results demonstrate the superiority of the proposed method across various DNA and protein sequence editing tasks. It consistently outperforms other baselines by generating sequences with fewer edits, enhanced properties, and greater diversity

### Weaknesses
 * Lack of Training Details: The paper lacks sufficient information regarding the training process of the policy. It should provide more details on the training data used, the methodology for updating parameters, and the specific hyperparameters employed in the process. Specifically, the architecture of the neural network used for the flow function is not clearly described. The paper should specify the number of layers, the type of activation functions, and the optimization algorithm used. Furthermore, the paper does not discuss the batch size, learning rate, or any regularization techniques applied during training. The absence of these details makes it difficult to reproduce the results.
* Unclear Literature Review: The literature review in the paper needs improvement. It is not adequately clear what the main contribution of the proposed method is, and how it distinguishes itself from existing work, particularly in relation to the utilization of GFlowNet for sequence generation. The paper should provide a more explicit and comparative analysis of related work. The review should discuss how the proposed method differs from existing GFlowNet-based sequence generation methods, especially those that also use a stochastic policy for sequence generation. It should also clarify the novelty of the proposed approach compared to other sequence editing techniques.
* Ambiguity in Key Innovation: The claim that GFNSeqEditor can produce novel sequences with improved properties lacks clarity regarding the key innovation driving these contributions. The paper should better articulate what novel techniques or insights lead to the claimed improvements, thereby enhancing the reader's understanding of the method's unique value. The paper needs to explain the specific mechanism by which the proposed method identifies sub-optimal positions for editing and how this differs from random or other heuristic-based editing strategies. The paper should also clarify how the stochastic editing policy contributes to the diversity of edited sequences and why this is an improvement over deterministic editing approaches.

### Questions
See the comments in Weakness section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces an innovative algorithm called GFNSeqEditor, which is specifically crafted to enhance sequences by optimizing their desired properties. GFNSeqEditor harnesses the power of pretrained flow functions and devises a set of destructive operations, whether tokens are modified or not. It then reconstructs the altered tokens using these pretrained flow functions. The process of destruction and subsequent reconstruction is governed by three crucial hyperparameters: $\lambda$, $\alpha$, and $\delta$. These hyperparameters play a pivotal role in achieving a balance between exploration and exploitation, while also managing the trade-offs and risks associated with expected improvements.

The authors provide a comprehensive analysis of these proposed hyperparameters, which intuitively guide the algorithm's behavior. To evaluate its effectiveness, GFNSeqEditor is benchmarked against classical editing methods across three distinct sequential generation tasks.

### Strengths
This paper excels in storytelling, skillfully introducing a promising generative model for sequence editing. The approach itself is novel and the underlying concept is commendable. The subsequent algorithm, while simple, remains straightforward, and the mathematical analysis of the newly introduced hyperparameters is intuitively presented. Overall, this paper is highly accessible and a pleasure to read.

### Weaknesses
The primary weakness of this paper lies in its experimental validation. In my opinion, the experiments conducted here fall short of adequately substantiating the proposed idea. There are several issues that need addressing:

**Pretraining Discrepancy**: One notable concern is the difference in the starting points for experimentation. While this work leverages pretrained GFN models, other baselines begin from scratch. This discrepancy could potentially lead to an unfair comparison.

**Baseline Variety**: The baseline comparisons should extend beyond the scope of other generative models and optimization techniques in biological sequence design. It would be beneficial to incorporate baseline methods such as offline model-based optimization [1], which are tailored to extrapolate sequences from offline datasets, thereby yielding "improved sequences."

**Evolutionary Algorithms**: To provide a more comprehensive perspective on the proposed approach, the paper could benefit from the inclusion of promising evolutionary algorithms specifically designed for biological sequence design [2].

**Comparison with GFN Baselines**: Additionally, conducting a thorough comparison with GFN baselines would be valuable in demonstrating the relative strengths and weaknesses of the proposed method when contrasted with models of similar architecture.

### Questions
1. Could you please elaborate on the process you used for pre-training GFN?

2. Have you conducted a comparison with baseline models (e.g., Seq-to-Seq) using the pretrained GFN as a component?

3. Does this algorithm demonstrate improvements in scalability?

4. Is this algorithm more beneficial than naive search algorithms based on pretrained policies, such as beam-search or MCTS?

5. Have you performed experiments related to Theorem 1 and 2? Inclusion of such experiments would likely enhance the overall quality of the paper.

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This submission isn concerned with the application of GFNs to sequence modifications. I’m not up to date with the relatively large number of works on similar approaches. The related work section appears in the supplementary material and does not attempt to discuss the differences between this paper and the papers listed there. This is a key issue that most be resolved. Also there is no comparison with earlier GFN methods: is there any for these problems? These concerns have made me give a lower score than what I otherwise would have given. I have minor comments and questions below, but I really enjoined reading this submission. It provides a description of the method at hand as well as the general GFN approach on very well chosen level. It is mostly well written. Moreover, the approach make sense and the results are good. I would like to accept it, but the above issue should be resolved.

### Strengths
Well written, technically strong, good resuls.

### Weaknesses
Poorly described relation to previous research and unclear if compared with the right methods. Also there is no comparison with earlier GFN methods: is there any for these problems? These concerns have made me give a lower score than what I otherwise would have given. I have minor comments and questions below, but I really enjoined reading this submission. It provides a description of the method at hand as well as the general GFN approach on very well chosen level. It is mostly well written. Moreover, the approach make sense and the results are good.

* that can provide consistency condition, Bengio et al. (2021) formulates ow- matching loss function as follows: LFM(s; θ) = log P∀s′:s′→s Fθ(s′ → s) P′′′′ Fθ(s → s′′) . (4) Moreover, as an alternative objective function 
Page 3 
Sure but which do you use? 
* 2  R(x)
Page 3 
Not defined here. 
* GFlowNet’s ow function Fθ(·) to identify sub-optimal positions of x, and subsequently replace the sub-optimal parts with newly sampled edits based on the stochastic policy π(·). pretrained ow function Fθ(·) Page 4 
At this point its implementation is not clear or why it can be pre trained 
* For instance for the DNA sequence x = ‘ATGTCCGC’, appending token a = ‘C’ to x:2, we get x:2 + a = ‘ATC’. 
Page 4 
I would guess that this is an insert operation on x, but it is not clear from the description, which actually suggests that the suffix from position t+1 is removed from x.
New guess: you are stepwise building a sequence and you either use the character from the given sequence or another. You should make this more clear. 
* 5  can
Page 4 
Would 
* 6  Pa′∈A Page 4 
It should be made clear that the given character x_t always belongs to the available actions. 
* 7  chosen by the algorithm Page 4 
Point out how or, alternatively, where you describe it. 
* 8  regularization parameter λ allows tuning Page 5 
Point out how it is set or where you describe it. 
* 9  RF,T represents the reward of a sequence with length T generated using the ow function Fθ(·) 
Page 5 
It IS the reward. Formulate it as a rv with the distribution induced by the flow function, with reference to the correct equation. 
* 10  Levenshtein  Page 6 
Spelling. 

* Higher binding activity is preferable Page 6 
In what sense? It may not be so in a biological system. 
* 12  diversity Page 7 
You need a better measure that also takes the improvement into account. 
* 13  14.34 Page 7 
This should be in bold, right?

### Questions
* that can provide consistency condition, Bengio et al. (2021) formulates ow- matching loss function as follows: LFM(s; θ) = log P∀s′:s′→s Fθ(s′ → s) P′′′′ Fθ(s → s′′) . (4) Moreover, as an alternative objective function  Page 3  Sure but which do you use?  
* 2  R(x) Page 3  Not defined here.  
* GFlowNet’s ow function Fθ(·) to identify sub-optimal positions of x, and subsequently replace the sub-optimal parts with newly sampled edits based on the stochastic policy π(·). pretrained ow function Fθ(·) Page 4  At this point its implementation is not clear or why it can be pre trained  
* For instance for the DNA sequence x = ‘ATGTCCGC’, appending token a = ‘C’ to x:2, we get x:2 + a = ‘ATC’.  Page 4  I would guess that this is an insert operation on x, but it is not clear from the description, which actually suggests that the suffix from position t+1 is removed from x. New guess: you are stepwise building a sequence and you either use the character from the given sequence or another. You should make this more clear.  
* 5  can Page 4  Would  
* 6  Pa′∈A Page 4  It should be made clear that the given character x_t always belongs to the available actions.  
* 7  chosen by the algorithm Page 4  Point out how or, alternatively, where you describe it.  
* 8  regularization parameter λ allows tuning Page 5  Point out how it is set or where you describe it.  
* 9  RF,T represents the reward of a sequence with length T generated using the ow function Fθ(·)  Page 5  It IS the reward. Formulate it as a rv with the distribution induced by the flow function, with reference to the correct equation.  
* 10  Levenshtein  Page 6  Spelling. 

* Higher binding activity is preferable Page 6  In what sense? It may not be so in a biological system.  
* 12  diversity Page 7  You need a better measure that also takes the improvement into account.  
* 13  14.34 Page 7  This should be in bold, right?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

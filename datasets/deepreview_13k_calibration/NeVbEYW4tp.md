# Efficient Test-Time Prompt Tuning for Vision-Language Models

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 5, 6, 3

## Abstract
Vision-language models have showcased impressive zero-shot classification capabilities when equipped with suitable text prompts. Previous studies have shown the effectiveness of test-time prompt tuning; however, these methods typically require per-image prompt adaptation during inference, which incurs high computational budgets and limits scalability and practical deployment.
To overcome this issue, we introduce Self-TPT, a novel framework leveraging Self-supervised learning for efficient Test-time Prompt Tuning.
The key aspect of Self-TPT is that it turns to efficient predefined class adaptation via self-supervised learning, thus avoiding computation-heavy per-image adaptation at inference.
Self-TPT begins by co-training the self-supervised and the classification task using source data, then applies the self-supervised task exclusively for test-time new class adaptation.
Specifically, we propose Contrastive Prompt Learning (CPT) as the key task for self-supervision. CPT is designed to minimize the intra-class distances while enhancing inter-class distinguishability via contrastive learning.
Furthermore, empirical evidence suggests that CPT could closely mimic back-propagated gradients of the classification task, offering a plausible explanation for its effectiveness.
Motivated by this finding, we further introduce a gradient matching loss to explicitly enhance the gradient similarity.
We evaluated Self-TPT across three challenging zero-shot benchmarks. The results consistently demonstrate that Self-TPT not only significantly reduces inference costs but also achieves state-of-the-art performance, effectively balancing the efficiency-efficacy trade-off.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors proposed Self-TPT, an efficient framework for test-time prompt tuning. This framework integrates contrastive prompt tuning (CPT) during the source prompt learning phase to cultivate more robust and generalizable feature representations. It applies CPT during test-time adaptation to improve the understanding of new classes and introduces a gradient matching loss in the source prompt learning phase to enhance the gradient correlation between CPT and classification tasks. Evaluation on three challenging zero-shot benchmarks shows that Self-TPT significantly reduces inference costs while achieving state-of-the-art performance, effectively balancing the trade-off between efficiency and efficacy.

### Strengths
1.The authors constructed contrastive prompt learning to enhance class differences and further strengthened this correlation through gradient matching. The idea of varying the position of the class token for text augmentation is novel to me.

2.The authors conducted comprehensive comparative experiments on three challenging benchmark datasets using their proposed method. The results demonstrated the method's outstanding performance.

3.The proposed Self-TPT method has lower inference computational costs, highlighting its potential for scalable stability in larger visual language models.

### Weaknesses
1.The authors vary the insertion points of the class token within prompt sequences as data augmentation to create positive pairs. However, the authors fail to give a convincing argument as to why that should lead to a better performance. For example, how did the authors decide to position the class token at the front, middle, and end, rather than choosing the positions randomly? The choice of these specific positions seems arbitrary and lacks justification in terms of how it might encourage the model to learn more robust feature representations compared to other augmentation strategies.

2.It is hard to convince me that applying a strong constraint (the GM loss) on contrastive loss and the CE loss? Constrastive loss is a more robust one possibly with better generalization ability, while the CE loss has the absolutely right discriminative information. I cannot see obviously strong relation. Exp in Table 5c, cannot convince me. Better provide more evidence or theoretical analysis. The gradient matching loss seems to force alignment between two objectives that may not inherently be aligned, potentially hindering the optimization process. The authors should provide a more detailed explanation of why this constraint is beneficial and how it avoids potential conflicts between the two losses.

3.In the prompt learning process of Stage 1, how are the weights among Lce, LCPT, and LGM distributed? The authors need to provide more relevant experimental results. I would also suggest authors to compare their method with more recent  studies, there are many related studies in 2024.

4. There may be a writing error in Table 5, where 'w/o hand' should probably be 'w/o end' ?

### Questions
Refer to weakness,

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Self-TPT, a novel framework for efficient test-time prompt tuning that addresses computational inefficiencies in existing methods. It proposes the Contrastive Prompt Learning (CPT) to minimize the intra-class distance, and a gradient matching loss to further enhance it.

### Strengths
1.	The approach is efficient to test-time adaptation that significantly reduces computational costs.
2.	The Comprehensive experiments across multiple datasets shows the effectiveness.

### Weaknesses
1.	The novelty is not significant, as leveraging multiple prompts is proved to be useful in Kgcoop and Promptalign paper, and the Gradient matching loss provide very little improvement and may loss performance in some settings, as shown in table 5c.
2.	Do you need more prompts than others, since you may need three more prompts for CPT.

### Questions
1.	Can it be applied with existing prompt learning methods, like CoOp + self-TPT
2.	In table 5c, what is the experiment setting for the first line? I assume it should has the same numbers as line 3 in table 5a, but they are different. Could you clarify that?

### Soundness
2

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
This paper proposes Contrastive Prompt Tuning (CPT). CPT is a text-only self-supervised object to refine class embedding. This additional refinement improves standard supervised prompt learning. Since CPT is text-only, it can also be applied to target class names, without accessing the test images like Test-time Prompt Tuning (TPT). There is also a finding on gradient similarity of CPT and classification task, which motivates the gradient matching loss to further improve the performance.

### Strengths
- CPT during supervised prompt learning does complement the supervised objective.
- Since CPT is text-only, it can also be applied to target class names, without accessing test images. This avoids per-sample optimization, which is costly.
- CPT partially mimics supervised learning gradient, and motivated by this, the paper proposes a gradient matching loss to further enhance the performance.
- good experiments to support the findings in the paper

### Weaknesses
Since CPT does not use test images, it can also be treated just as a additional loss to supplement supervised prompt learning. 
- might be good to compare with more recent prompt learning approaches (Any-shift prompting, PromptKD etc), and not just focus on test-time prompt tuning approaches, where there are less recent baselines.
- can CPT also be combined with TPT for each sample like other prompt tuning approaches? self-TPT-v just do output ensemble?

### Questions
See weaknesses

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
While previous test-time prompt tuning methods have demonstrated their effectiveness, they are computationally expensive as they require multiple forward and backward passes on each test sample. In this paper, the authors propose an efficient test-time prompt tuning technique to mitigate this overhead through self-supervised learning on predefined class names. To enhance the alignment between the classification task and the self-supervised task, they further introduce a gradient matching loss. On base-to-new, cross-dataset, and domain generalization benchmarks, the proposed method achieves superior efficiency and performance compared to state-of-the-art approaches.

### Strengths
- The paper is well-written and easy to follow.  
- The proposed method is simple and straightforward to implement.  
- The motivation to reduce test-time overhead is meaningful. The method avoids multiple forward passes and real-time tuning, making it practical for implementation.

### Weaknesses
1.   The proposed method faces a fundamental technical flaws when adapting models to new target domains that share the same label space as the source domain. The unsupervised prompt learning framework operates solely on the text branch and is designed to adapt to new class names. However, it overlooks potential domain shifts in the image inputs. For example, if the source domain consists of real photos and the target domain consists of sketches with the same labels, the proposed method is unlikely to adapt effectively to the sketches without leveraging the information from the input images. This raises doubts about the results reported in Table 4. I conjecture the improvements may instead stem from prompt ensembling.  

2.   The design of the ablation studies is problematic. It is well established that learning multiple soft prompts can outperform a single prompt [1,2]. From my experience with prompt tuning, using four prompts and properly ensembling them can improve accuracy by more than 1% (as also demonstrated in the G+E row of Table 2 in [1]). The ablation studies, however, do not include the performance of comparable baselines that use similar ensembling techniques.  

In domain generalization settings, the training and testing datasets share the same class names (no changes in class priors.). **Theoretically, this should negate any significant improvements achieved through your method**. Yet, improvements are still observed in your results. I find this inconsistency unconvincing. 

The results in Table 5(a) **are not the experiment I referred to**.  My concern lies with the effectiveness of CPT. The experiment should involve learning 4 soft prompts independently using cross-entropy and then ensembling them.

### Questions
Please refer to the weakness.

### Soundness
2

### Presentation
4

### Contribution
2

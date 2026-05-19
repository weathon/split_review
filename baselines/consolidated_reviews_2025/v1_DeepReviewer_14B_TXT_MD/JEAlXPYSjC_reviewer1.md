### Summary

This paper demonstrates that CLIP models pre-trained on smaller datasets may be undertrained. The authors propose a straightforward additional training procedure and show its effectiveness, which achieves competitive results compared to existing approaches.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

1 poor

### Strengths

1. The authors demonstrate that CLIP models pre-trained on smaller datasets may be undertrained. 
2. The authors propose a simple additional training procedure and show its effectiveness.

### Weaknesses

#### Some Related Works


#### comment

1. The additional training procedure is too simple, lacking novelty.
2. There is a lack of theoretical analysis regarding why this method is effective.
3. The results in Table 7 do not demonstrate a significant advantage over other methods.

### Suggestions

The paper's core idea, that CLIP models trained on smaller datasets may be undertrained, is interesting, but the proposed solution lacks sufficient depth and novelty. While simplicity can be a virtue, the additional training procedure, as presented, is essentially a basic fine-tuning approach. The authors should explore more sophisticated techniques to enhance the model's learning, such as incorporating adaptive learning rates, or using more advanced regularization methods. Furthermore, the current approach does not address the potential for overfitting during the additional training phase, which could limit its effectiveness on more complex datasets or tasks. A more rigorous exploration of the parameter space and training dynamics is needed to make a more compelling case for the proposed method.

The absence of theoretical justification is a significant weakness. The paper would greatly benefit from a theoretical analysis that explains why the additional training procedure is effective. This could involve analyzing the loss landscape of the CLIP model and how the proposed method helps the model escape local minima or saddle points. For example, the authors could investigate the gradient flow during the additional training phase and compare it to the initial training phase. This would provide a deeper understanding of the method's behavior and help to identify the conditions under which it is most effective. Without such analysis, the paper remains largely empirical and lacks the necessary theoretical underpinnings to support its claims. The authors should also consider exploring the connection between the proposed method and existing theories on transfer learning and generalization.

Finally, the empirical results presented in Table 7 do not convincingly demonstrate the superiority of the proposed method over existing approaches. The improvements are marginal and do not justify the claim of achieving competitive results. The authors should conduct a more comprehensive evaluation, including a wider range of datasets and tasks, and compare their method to a broader set of baselines. It would also be beneficial to analyze the performance of the proposed method under different training conditions, such as varying the amount of additional training data or the learning rate. A more thorough empirical analysis is needed to establish the practical value of the proposed method and to demonstrate its advantages over existing techniques.

### Questions

1. Why does the proposed additional training procedure only include 1 to 3 epochs? Is this too arbitrary?
2. What is the difference between the proposed additional training procedure and the learning rate warm-up technique?
3. Could the authors provide the results of CLIP models pre-trained on larger datasets, such as CLIP (ViT-B-32, OpenAI), CLIP (ViT-L-14, OpenAI), or EVA-CLIP?

### Rating

3: reject, not good enough

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********

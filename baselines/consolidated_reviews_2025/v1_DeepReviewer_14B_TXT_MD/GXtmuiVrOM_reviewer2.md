### Summary

The authors propose a novel domain randomization approach that automatically shapes dynamics distributions during training in simulation without requiring real-world data. Their approach, DORAEMON, directly maximizes the entropy of the training distribution while retaining generalization capabilities. In achieving this, DORAEMON gradually increases the diversity of sampled dynamics parameters as long as the probability of success of the current policy is sufficiently high. They empirically validate the consistent benefits of DORAEMON in obtaining highly adaptive and generalizable policies as opposed to representative baselines from the DR literature. Notably, they also demonstrate the Sim2Real applicability of DORAEMON through its successful zero-shot transfer in a robotic manipulation setup under unknown real-world parameters.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The idea of maximizing the entropy of the training distribution while retaining generalization capabilities is interesting and novel.
- The paper is well-written and easy to follow.
- The empirical results show that DORAEMON outperforms other baselines in obtaining highly adaptive and generalizable policies and achieves good sim2real transfer.

### Weaknesses

#### Some Related Works


#### comment

 - The experiment is conducted in only one sim2real environment. More environments are needed to show the effectiveness of the proposed method.
- The performance of the proposed method is very sensitive to the choice of hyper-parameters, which makes it less practical in real-world applications.

### Suggestions

The paper's primary weakness lies in the limited scope of its experimental validation, specifically the use of a single sim2real environment. While the proposed method, DORAEMON, demonstrates promising results in the presented scenario, the lack of diversity in testing environments raises concerns about its generalizability. To address this, the authors should evaluate DORAEMON across a wider range of sim2real tasks, encompassing different robot morphologies, task complexities, and environmental conditions. For example, experiments could include manipulation tasks with varying object properties (e.g., friction, mass, compliance), locomotion tasks on different terrains, or tasks involving more complex interactions with the environment. This would provide a more robust assessment of the method's capabilities and limitations, and better demonstrate its applicability to real-world robotic problems. Furthermore, the evaluation should include a more detailed analysis of the transfer gap, examining how the performance degrades when moving from simulation to real-world scenarios, and identifying potential failure modes.

Another significant concern is the sensitivity of DORAEMON to hyperparameter choices. The paper acknowledges this sensitivity, but it is not sufficiently addressed. The authors should provide a more thorough analysis of how different hyperparameter settings affect the performance of the method, including the learning rate, the entropy regularization coefficient, and the parameters related to the dynamics distribution. This analysis should not only focus on the final performance but also on the training stability and convergence speed. Furthermore, the authors should investigate methods to reduce this sensitivity, such as adaptive hyperparameter tuning or robust optimization techniques. Without a clear understanding of how to choose hyperparameters and how they affect the performance, the practical applicability of the method is limited. The authors should also provide clear guidelines for selecting appropriate hyperparameter values for new tasks and environments, which would greatly enhance the usability of the proposed approach.

Finally, the paper would benefit from a more detailed comparison with existing domain randomization techniques. While the paper mentions that DORAEMON outperforms other baselines, it does not provide a thorough analysis of the differences between these methods. A more detailed comparison should include an analysis of the strengths and weaknesses of each method, as well as a discussion of the specific scenarios where each method performs best. This would help to better understand the contributions of DORAEMON and its potential advantages over existing approaches. The authors should also consider comparing DORAEMON with more recent domain randomization methods, which may have addressed some of the limitations of the baselines used in the paper. This would provide a more comprehensive evaluation of the proposed method and its place within the broader landscape of sim2real transfer techniques.

### Questions

- How does the proposed method perform in other sim2real environments?
- How to choose the hyper-parameters of the proposed method?

### Rating

6: marginally above the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********

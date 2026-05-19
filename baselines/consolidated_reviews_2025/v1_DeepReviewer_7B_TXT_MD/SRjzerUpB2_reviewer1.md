### Summary

This paper proposes a new method for offline reinforcement learning with sparse policies, which is based on a two-stage actor-critic framework. The first stage learns a fat policy and the second stage learns a sparse policy. The authors instantiate this method with the general $q$-Gaussian family, and verify the effectiveness of the proposed method on a safety-critical treatment simulation and the standard D4RL MuJoCo benchmark.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The paper addresses an important problem in offline reinforcement learning, which is learning a sparse policy from offline data.

### Weaknesses

#### Some Related Works

[1] Supported policy optimization: Reinforcement learning with safe actions.
[2] Supported policy optimization with safety constraints.
[3] Supported policy optimization with safety constraints: A survey.

#### comment

1. The proposed method is not novel. The two-stage learning framework is a common approach in reinforcement learning, and the use of $q$-Gaussian policies has been explored in previous works [1, 2, 3]. The paper does not adequately differentiate its approach from these existing methods, particularly in terms of the specific mechanisms that enable it to handle out-of-support actions in offline settings. The novelty of the approach is further diminished by the lack of a clear explanation of how the proposed method addresses the unique challenges of offline RL with sparse policies, beyond what is already known about two-stage learning and $q$-Gaussian policies.

2. The experimental results are not convincing. The proposed method is only compared with a few baselines, and the performance of the proposed method is not consistently better than the baselines. The paper lacks a thorough comparison with a wider range of state-of-the-art offline RL algorithms, particularly those that also utilize sparse policies or similar techniques. The limited scope of the experiments makes it difficult to assess the true potential and robustness of the proposed method. Furthermore, the paper does not provide a detailed analysis of the performance differences between the proposed method and the baselines, which would be necessary to understand the strengths and weaknesses of the approach.

3. The paper does not provide a clear explanation of how the proposed method addresses the out-of-support action issue in offline RL. While the paper mentions that the method uses a fat policy to generate actions and a sparse policy to learn from them, it does not provide a detailed explanation of how this process mitigates the problem of out-of-support actions. The paper should provide a more rigorous analysis of the proposed method's ability to handle out-of-support actions, including a discussion of the theoretical underpinnings and empirical evidence.

### Suggestions

The paper needs to more clearly articulate the novelty of its approach and provide a more thorough comparison with existing methods. Specifically, the authors should clearly differentiate their method from existing two-stage learning frameworks and $q$-Gaussian policy approaches. This should include a detailed explanation of how the proposed method addresses the specific challenges of offline RL with sparse policies, such as the issue of out-of-support actions. The authors should also provide a more rigorous theoretical analysis of their method, including a discussion of its convergence properties and its ability to handle out-of-support actions. Furthermore, the paper should include a more comprehensive set of experiments, comparing the proposed method with a wider range of state-of-the-art offline RL algorithms. This should include a detailed analysis of the performance differences between the proposed method and the baselines, including a discussion of the strengths and weaknesses of each approach. The authors should also provide a more detailed explanation of the experimental setup, including the specific hyperparameters used and the evaluation metrics employed.

To address the concerns about the lack of novelty, the authors should focus on highlighting the unique aspects of their approach and how it differs from existing methods. This could include a discussion of the specific mechanisms that enable the proposed method to handle out-of-support actions in offline settings, as well as a comparison of its performance with existing methods on a wider range of tasks. The authors should also provide a more detailed explanation of the theoretical underpinnings of their method, including a discussion of its convergence properties and its ability to handle out-of-support actions. This should include a rigorous analysis of the proposed method's ability to learn a sparse policy from offline data, and how it compares to existing methods that also utilize sparse policies or similar techniques. The authors should also provide a more detailed explanation of the experimental setup, including the specific hyperparameters used and the evaluation metrics employed.

Finally, the paper should provide a more detailed explanation of how the proposed method addresses the out-of-support action issue in offline RL. This should include a discussion of the specific mechanisms that enable the proposed method to handle out-of-support actions, as well as a comparison of its performance with existing methods on a wider range of tasks. The authors should also provide a more detailed explanation of the theoretical underpinnings of their method, including a discussion of its convergence properties and its ability to handle out-of-support actions. This should include a rigorous analysis of the proposed method's ability to learn a sparse policy from offline data, and how it compares to existing methods that also utilize sparse policies or similar techniques. The authors should also provide a more detailed explanation of the experimental setup, including the specific hyperparameters used and the evaluation metrics employed.

### Questions

1. How does the proposed method address the out-of-support action issue in offline RL?
2. What is the novelty of the proposed method compared to existing two-stage learning frameworks and $q$-Gaussian policy approaches?
3. How does the proposed method perform compared to a wider range of state-of-the-art offline RL algorithms?

### Rating

5

### Confidence

4

**********

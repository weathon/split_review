# Revisiting Generative Policies: A Simpler Reinforcement Learning Algorithmic Perspective

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 5, 8, 5

## Abstract
Generative models, particularly diffusion models, have achieved remarkable success in density estimation for multimodal data, drawing significant interest from the reinforcement learning (RL) community,
especially in policy modeling in continuous action spaces.
However, existing works exhibit significant variations in training schemes and RL optimization objectives, and some methods are only applicable to diffusion models.
In this study, we compare and analyze various generative policy training and deployment techniques, identifying and validating effective designs for generative policy algorithms.
Specifically, we revisit existing training objectives and classify them into two categories, each linked to a simpler approach.
The first approach, Generative Model Policy Optimization (GMPO), employs a native advantage-weighted regression formulation as the training objective, which is significantly simpler than previous methods.
The second approach, Generative Model Policy Gradient (GMPG), offers a numerically stable implementation of the native policy gradient method.
We introduce a standardized experimental framework named \textit{GenerativeRL}.
Our experiments demonstrate that the proposed methods achieve state-of-the-art performance on various offline-RL datasets, offering a unified and practical guideline for training and deploying generative policies.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work systematically analyzes existing diffusion-based offline reinforcement learning methods, including their training and inferring strategy. In summary, this work summarizes existing methods into two classes: Generative Model Policy Optimization (GMPO) and Generative Model Policy Gradient (GMPG), which mainly consider the forward KL and inverse KL respectively. In detail, GMPO directly considers advantage-weighted regression formulation and GMPG offers a numerically stable implementation of the native policy gradient method. This work also provides a standardized experimental framework named GenerativeRL for fair comparison.

### Strengths
- Providing a unified perspective is important for the community.

- This work has provided detailed codes and instructions. And the standardized experimental framework is meaningful for comparing different algorithms.

- This work consider more general generative models, including diffusion models and flow models.

### Weaknesses
 - My major concern is about the novelty of this work. Analyzing the forward KL/ inverse KL seems to be a consensus in the community. As the authors have mentioned, lots of previous work has discussed these two formulations, so are any new theoretical insights or empirical findings that emerged from their systematic analysis that go beyond prior work? Although that, I still appreciate the authors' efforts to provide a unified view and codebase, which is beneficial for further research.

- The performance of GMPO and GMPG seems similar to previous methods in locomotion tasks (table 3) and weaker than baselines in antmaze tasks (table 11, several baselines > 75, while GMPO 73.8 and GMPG 66.5). Why does this phenomenon exist, and is there some specific analysis about it? For example, are there any significant characteristics in locomotion tasks and antmaze tasks that result in the proposed algorithm, especially GMPG, performing poorly in the antmaze tasks?

- How do you calculate $\log \pi$ of the diffusion policies in GMPG? The introduction in lines 316-327 is too brief and the explanation in the appendix should be moved partially to the main text.

### Questions
See weaknesses above.

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
2

### Summary
The paper presents an unified framework for training flow and diffusion models for offline reinforcement learning algorithms. Authors classify existing training objectives into two categories and linked to simpler approaches, GMPO and GMPG. The paper also proposes a standardized experimental framework for evaluating various generative policies.

### Strengths
There are several works which utilize generative models for parametrizing policy for offline RL due to various reasons (multi-modal distribution, controllability, …). I think this paper has a significant contribution on analyzing prior generative policies.

Furthermore, I saw multiple papers in Offline RL reproduce the baselines by their own and the fluctuation of the performance is very large. I think the comprehensive evaluation through GenerativeRL may resolve this issue.

### Weaknesses
One of the my major concerns is the position of the paper. It is a bit confused that authors want to build a unified benchmark suite for evaluating various generative policies for RL or propose an algorithm that can be easily applied to train generative policies for RL. For the former, it will be better to include some details on experimental setup and training & evaluation procedure. For the latter, more analysis or stronger experimental results should support the author's claim.

Here are some minor concerns:

- While the paper focus on offline RL algorithms, there are several works which utilize generative policies for online reinforcement learning [1, 2]. It might be better to cover those algorithms or the title should be revised to Offline RL.

- It seems that hyperparameter $\beta$ is heavily tuned for different environment and the range of value is quite large. Could authors verify the details on hyperparameter tuning procedure of proposed approaches?

- While the authors claim that GMPO and GMPG achieves competitive performance compared to Diffusion-QL without several tricks such as joint training, generating multiple actions and choosing one action, etc., these implementation-level tricks can lead to significant performance improvements and should not be ignored. The paper should acknowledge that the performance gains of Diffusion-QL might not be solely attributed to the diffusion policy itself, but also to these implementation details.

### Questions
In D4RL benchmark, Diffusion-QL achieves state-of-the-art performance even though other baselines are more recently proposed. Could authors validate why such phenomena happens?

In figure 1, what is the optimal policy in this plot exactly? Does it indicate optimal policy introduced in Eq (5)? Is it tractable?

### Soundness
3

### Presentation
3

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
This paper 1. summarizes previous optimization methods for diffusion policies and classifies them into two categories. 2. proposes a simpler optimization method for each optimization category. The paper also abstracts existing diffusion optimization techniques into a Python library and (maybe) plans to open-source it. The above algorithms are compared in detail in standard benchmarks.

### Strengths
1. This is the first work I know that integrates various diffusion policy optimization algorithms into one framework. I believe this is beneficial to the community.
2. The work presents a clear theoretical comparison of existing diffusion optimization methods and unifies them in one framework. This is good contribution.
3. The proposed GMPO and GMPG algorithm is theoretically foundationed and yields good performance compared with previous work.
4. The paper is well-presented. Table 1 and Table 2 is extremely helpful in understanding current lines of work.

### Weaknesses
1. I have some concerns about the novelty of GMPO. Despite its simplicity, I believe this is somewhat very similar to the AWR algorithm, just that it optimizes a diffusion policy instead of a Gaussian policy. Also, this algorithm has already been verified in the image generation field.

Kimin Lee, Hao Liu, Moonkyung Ryu, Olivia Watkins, Yuqing Du, Craig Boutilier, Pieter Abbeel, Mohammad Ghavamzadeh, and Shixiang Shane Gu. Aligning text-to-image models using human feedback. arXiv preprint arXiv:2302.12192, 2023. 3, 6

2. When applying GMPG, as I understand, Neural ODE needs to be leveraged in order to estimate logp of \mu. I'm concerned about the computation efficiency of this method. Could you compare it with SRPO and Diffusion-QL? Also, I think for GMPG, your policy model has to be a Gaussian but cannot be a diffusion policy. For Diffusion QL, your policy can be a Diffusion policy. Is this correct?

3. There are mistakes in the inference scheme for SfBC, and Diffusion QL, and IDQL in Table 2. I recall for Diffusion QL and IDQL, they simply take [max] of action candidate Q values, not softmax. For SfBC, it uses [softmax] rather than [max]. Not entirely sure about the first two. Please recheck their code implementations.

### Questions
1. When will the codebase go public? 
2. I suggest annotating each algorithm and indicating which category they come from in Table 2. For instance, Diffusion QL and SRPO are reverse KL methods.   QGPO and GMPO are forward KL. SfBC and IDQL are forward KL (or sampling-based?)  This should be more clear to readers.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper revisits prior research on generative policies and provides a comprehensive comparison and analysis of various learning objectives and optimization techniques, proposing a simpler approach to reinforcement learning. The paper introduces two key methods: Generative Model Policy Optimization (GMPO) and Generative Model Policy Gradient (GMPG). GMPO leverages a more straightforward advantage-weighted regression method, enabling efficient training, while GMPG introduces a numerically stable policy gradient approach. Additionally, the paper presents an experimental 'software' named GenerativeRL, designed to evaluate the performance of generative policy algorithms and demonstrate their consistent results across multiple datasets. Through this work, the authors propose a novel methodology combining generative models with reinforcement learning, simplifying the training process without compromising performance.

The key concepts covered in the paper are as follows:
1. Generative Policy: A method in reinforcement learning that utilizes generative models to represent the distribution of actions when learning a policy. This is particularly effective in continuous action spaces and is exemplified by diffusion models and flow models, which excel in modeling multi-modal data.
2. GMPO (Generative Model Policy Optimization): A training method that uses advantage-weighted regression to optimize policies. GMPO simplifies the training process, offering stability and efficiency without the need for behavior policy, while extracting optimal policies based on environmental rewards.
3. GMPG (Generative Model Policy Gradient): A variant of the policy gradient method that provides a numerically stable implementation. Unlike GMPO, GMPG builds on pretrained policies and computes gradients over continuous time.
4. GenerativeRL Framework: A standardized experimental framework designed to evaluate and compare different generative policy learning algorithms. It decouples the generative model from the reinforcement learning components, providing unified API, flexible data formats and shapes, auto-grad support, and diverse generative model integration.

### Strengths
- GMPO and GMPG effectively simplify complex training methods, operating efficiently while delivering optimal policies without performance degradation.
- The proposed methods demonstrate comparable when compared to state-of-the-art algorithms across various datasets, consistently proving their stability and robustness in different settings.
- GenerativeRL Framework: The detailed description of the framework provided in the appendix significantly enhances reproducibility, which is a strong point. (However, I have some reservations regarding the extent of the contribution attributed to this framework, which will be discussed in the weaknesses section.)

### Weaknesses
I raise several concerns about the overall structure of this paper.  
- Firstly, it is unclear whether the authors are proposing a "framework" or merely organizing "experimental code" more systematically.  
Secondly, it remains ambiguous whether the paper "classifies existing works into two categories(line 18 in abstract)" or surveys prior works, "identifies their limitations, and proposes two new algorithms" as a solution.

    - 3.1: The term "experimental framework" should be explicitly defined as referring to software. While the well-organized experimental code is appreciated, I question whether emphasizing it as a "framework" and a "contribution" is justified.

    - 3.2: The connection between GMPO, GMPG, and existing algorithms is not sufficiently clear. I also find the theoretical foundation of these algorithms lacking. Specifically:
        1. The introduction does not provide a thorough explanation of why these categories were chosen or how they were grouped. A more explicit revisit is needed. For example, if SfBC belongs to the GMPx class, and QGPO is also part of the GMPx class, it should be clarified what their common traits are, and why they were categorized together. Then, the paper could explain how the proposed GMPO and GMPG represent advances based on these categories.
        2. In Section 4.2: Previous Works on Generative Policy, while it is clear what improvements are needed, there is no clear categorization presented. Additionally, while systematically investigating inefficiencies and eliminating them is always a valuable academic contribution, there is no theoretical proof supporting the proposed methods. The paper gives reasons why the methods might be necessary, but it does not clearly show how they improve the situation.

- It is unclear whether this study focuses specifically on offline RL or is meant to be more broadly applicable to general RL.

- In the Related Works section, the connection between prior research and the present work is not sufficiently emphasized. The section reads more like a chronological listing without interpretation of the strengths, weaknesses, or the progression of improvements. It would also be helpful to introduce abbreviations (e.g., SfBC) in the Related Works section and explain the paper’s categorization in that context.

### Questions
- What does "Any" in Table 1 signify? If it only refers to DDPM and VPSDE, does that mean methods based on flow models are not covered? Or, are flow models also included under "Any"? (I understand "Any" includes flow but it confuse me.) Were there no prior algorithms using flow models, or were they intentionally excluded? In the introduction, it was mentioned that offline RL focuses on diffusion models—are there no flow-based methods in this domain? (line 44, Table 1)

- Can the proposed GMPO and GMPG methods be stably applied to more complex generative models beyond diffusion and flow models?

- Are there any reinforcement learning applications using generative policies that are not focused on offline RL? The scope of the research remains unclear to me.

- How well does the flexibility of the GenerativeRL framework extend to the compatibility with other reinforcement learning algorithms?

- The abbreviations DSM and CFM do not appear to be explained in "the front" of the paper (eqn 2,3). Could these be clarified?

### Soundness
3

### Presentation
1

### Contribution
2

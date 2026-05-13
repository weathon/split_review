# Gymnasium: A Standard Interface for Reinforcement Learning Environments

- Decision: Reject
- Avg Score: 7.25
- Scores: 5, 10, 6, 8

## Abstract
Reinforcement Learning (RL) is a continuously growing field that has the potential to revolutionize many areas of artificial intelligence. However, despite its promise, RL research is often hindered by the lack of standardization in environment and algorithm implementations. This makes it difficult for researchers to compare and build upon each other's work, slowing down progress in the field.
Gymnasium is an open-source library that provides a standard API for RL environments, aiming to tackle this issue. Gymnasium's main feature is a set of abstractions that allow for wide interoperability between environments and training algorithms, making it easier for researchers to develop and test RL algorithms. In addition, Gymnasium provides a collection of easy-to-use environments, tools for easily customizing environments, and tools to ensure the reproducibility and robustness of RL research.
Through this unified framework, Gymnasium significantly streamlines the process of developing and testing RL algorithms, enabling researchers to focus more on innovation and less on implementation details. By providing a standardized platform for RL research, Gymnasium helps to drive forward the field of reinforcement learning and unlock its full potential.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper attempts to address the lack of standardization in reinforcement learning environments. The paper’s library is able to be used in conjunction with a number of libraries, showing that it has been adopted across the field. The paper provides abstraction for environments through a set of fundamental spaces. The paper implements vectorization to enable parallelization across environments. The paper analyzes the increase in environment throughput with vectorization to show that this can provide substantial speedups to using the library.

### Strengths
Gym and now gymnasium is an essential part of reinforcement learning with many packages and works being built on top of or inspired by a similar methodology. The abstraction provided by the method is commonly used across reinforcement learning and is easy to use. The vectorization increases throughput of running an environment without significant overhead. The writing is fairly straightforward and it is easy to understand the methodology of the work. Without outside comparison, the results show that the vectorization is able to provide significant speedups. The use of vectorization is key to enable speed-up in performance.

### Weaknesses
Despite the use of the name recognition of the library, it is unclear if the improvements from OpenAI Gym to Gymnasium are comparable to the contributions from other RL libraries 2015-present. My main issue with the work is the lack of discussion and comparison with similar work. (In section 2 the paper details a number of comparable works that can use their framework but this is not sufficient to my point.) The paper should complement technical report details with meaningful comparisons to help researchers choose which library to use.

Reinforcement learning is going a massive change in environments due to parallelization but these benefits are from Jax and other GPU engines such as Madrona engine [1], not work created by this library so I do not think it is a fair claim that they can claim credit for those works. 

Other works have better vectorization such as Puffer [2] and I would expect a mention or comparison to similar libraries. The paper should explain why one should use Gymnasium versus competitors. It would be helpful to see comparisons across the same environments for each library.

RLlib [3], which is in the related work of the paper, shows substantial deployment and scalability for reinforcement learning on distributed training. 

Each of these papers regarding reinforcement learning libraries provide substantial merits for scaling reinforcement learning training. Though I think it is important to encourage RL infrastructure and environment development in reinforcement learning, it is unclear that a set of abstractions provided by Gymnasium have the same level of contribution as the other papers empirical efforts.

### Questions
There is still significant space available for additional results on other environments (which may be more complicated and thus show interesting ablations for synchronous and nonsynchronous methods) provided in Gymnasium. Why not provide additional examples of the work in the paper? There is plenty of room, and it will help show readers unfamiliar with your package about the library's use cases. See weaknesses for examples of papers with more extensive write-ups regarding libraries.

> We hope that this work removes barriers from DRL research and accelerates the development of safe, socially beneficial artificial intelligence.
How does this work do that? This claim is not defended by the experiments.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
The paper  introduces Gymnasium, a standardized API designed to improve interoperability and reproducibility in reinforcement learning (RL) research. Gymnasium, an update and extension of the OpenAI Gym, addresses issues such as inconsistent environment implementations and the need for easy experimentation and robust testing. Its main contributions include a unified API compatible with multiple RL libraries, support for both individual and vectorized environments, and novel features such as a functional API closely aligned with Partially Observable Markov Decision Processes (POMDPs), a structured approach to termination and truncation, and expanded support for algebraic spaces. Gymnasium also provides a suite of customizable benchmark environments that range from simple tabular MDPs to complex physical simulations using MuJoCo, helping to accelerate RL algorithm development and testing.

### Strengths
- By providing a consistent API, Gymnasium streamlines RL research, making it easier for researchers to compare and build upon previous work.
-The functional API enhances compatibility with theoretical frameworks like POMDPs and enables hardware-accelerated environments using libraries like JAX, which is beneficial for large-scale or computationally intensive applications.
- The built-in vectorization features (Sync and Async) support efficient parallelization of environments, which can significantly improve the performance of RL training processes.
- Gymnasium includes environments from basic MDPs to complex MuJoCo simulations, catering to various RL research needs and supporting a broad range of algorithms and approaches.

### Weaknesses
The choice between Sync and Async vectorization modes shows substantial performance variability depending on hardware, which could lead to inconsistencies across different systems or add complexity for users lacking high-performance resources.

### Questions
- Does Gymnasium include any tools or guidelines to help users choose the best vectorization mode (Sync vs. Async) based on their hardware?
- How does Gymnasium handle massively parallel or distributed training environments? Is there integration with cloud-based or cluster-based frameworks for larger-scale experiments?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper provides an overview of the widely-used Gymanasium open-source API for RL experiments. It describes the two approaches for interafcing to environments (standard Env class, and the FuncEnv functional API), discusses the difference between Termination and Truncation, the data types used for action and observation spaces, the role of VectorEnvs in enabling parallelisation of learning. It also reviews the built-in environments, related RL implementations and tool libraries, and alternative API libraries.

### Strengths
The paper provides a well-written, comprehensive overview of Gymnasium, which would be of use to a newcomer to this API.

Gymnasium itself is an extremely valuable contribution to the RL community, as evidenced by its widespread adoption.

### Weaknesses
There is little original content in this paper as it is basically replicating the documentation available through the Gymnasium website (https://gymnasium.farama.org/index.html).

The decision of whether to accept this paper or not really comes down to a philosophical question around the purpose of ICLR.

The Reviewer's Instructions ask us to consider the paper's value from the contribution of the ICLR community ("What is the significance of the work? Does it contribute new knowledge and sufficient value to the community? Note, this does not necessarily require state-of-the-art results. Submissions bring value to the ICLR community when they convincingly demonstrate new, relevant, impactful knowledge". From this perspective I don't think the paper has much value.  The vast majority of RL researchers that would attend ICLR would already be familiar with, and quite likely already using, Gymnasium. So there is little here that would be especially novel for attendees.

On the other hand we all know that publications at key venues like ICLR have considerable weight for career progression, and undoubtedly the authors deserve credit for their work in developing and maintaining this valuable resource. So there could be a case for acceptance on that basis.

This feels to me like a decision that perhaps needs to be made at a higher level in the conference hierarchy than reviewers?

My personal feeling is that this is perhaps the wrong venue for this work. If it is not accepted, I'd suggest the authors consider submitting to the Software Track of JMLR, as that is designed to support precisely this type of publication.

### Questions
I don't have any questions for the authors.

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces Gymnasium, an open-source library that provides a standard API for building RL environments. As a maintained fork of OpenAI Gym, Gymnasium offers enhanced features and interoperability across RL environments and training algorithms. Gymnasium has significantly outperformed the Gym in terms of built-in environments, application ecosystem, and operating efficiency. There is no doubt that Gymnasium has become the new standard interface in the RL community, which is expected to continue to drive forward the field.

### Strengths
It is natural to compare Gymnasium and the OpenAI Gym to highlight its strengths:

- **Active developer community**. As a maintained fork, Gymnasium has gained 7.1k stars, 450+ issues and, 750+ PRs on GitHub, which demonstrates a really active community. This open-source collaboration will make Gymnasium a comprehensive library that aligns with the latest direction of RL.
  
- **New `.step()` logic**. Gymnasium introduces the notions of episode
  **termination** and **truncation**. **Termination** ends an episode based on the agent reaching a specific state, like winning or failing, signaling the task is complete. **Truncation** stops an episode after a set time or a number of steps, even if the task isn't finished, helping to limit long-running tasks for practical experiments. Both concepts are important for controlling episode length and ensuring efficient learning in RL.
  
- **More built-in environments**. As compared to Gym, Gymnasium provides more built-in environments that cover more research areas, such as offline RL and meta RL. Gymnasium's team also integrated many old and important environments, such as MiniGrid, Procgen, and Meta-World.
  
- **Performance optimization**. The library's emphasis on **vectorized environments** allows researchers to parallelize experiments and improve performance without major changes to algorithms. The performance comparisons presented in the paper show significant gains with proper vectorization modes.
  
- **Functional API**. The introduction of a *FuncEnv* offers flexibility in programming paradigms and is better aligned with the POMDPs. It also allows for efficient usage of hardware accelerators like JAX.

### Weaknesses
Please refer to the questions part.

### Questions
Based on the presented paper and the reported progress on GitHub, I have the following questions:

- Indeed, Gymnasium is a great successor to Gym. But it is undeniable that there are still a large number of projects using Gym due to various reasons like old environments or dependencies. How will Gymnasium promote further popularization in the community?
  
- On the other hand, how does Gymnasium achieve better backward compatibility with old code? A section about the code compatibility should be added.
  
- In Gymnasium, the `.reset()` is re-implemented, and the `.seed()` method is deprecated. I don't see the necessity for this change, could you elaborate it further?
  
- In Section 2.1, more new libraries should be included, such as d2rlpy [1] (for offline RL), TorchRL [2], and RLLTE [3]. Dopamine is a bit too old.
  
- I did't see the future work section, which is quite important for the paper.
  
- Code examples should be included, which also need to demonstrate the difference between Gym and Gymnasium.
  
- I strongly recommend the authors to make a chart to illustrate the structure and new logic of Gymnasium.
  
- For Section 5, using a table that illustrates the built-in envs and related official envs (e. g., MiniGrid and Procgen) would be better. The authors can also highlight the potential research targets of these envs, such as Procgen is procedurally-generated and MiniGrid is for exploration.

- The performance benchmarks focus on relatively simple environments such as **Cartpole** and **Lunar Lander**. It would better to include a broader range of environments, particularly more challenging and high-dimensional ones, to demonstrate Gymnasium's true potential.
  

I'm pleased to increase my rating if my questions are addressed.

References

[1] Seno T, Imai M. d3rlpy: An offline deep reinforcement learning library[J]. Journal of Machine Learning Research, 2022, 23(315): 1-20.

[2] Bou A, Bettini M, Dittert S, et al. TorchRL: A data-driven decision-making library for PyTorch[C]//The Twelfth International Conference on Learning Representations.

[3] Yuan M, Zhang Z, Xu Y, et al. RLLTE: Long-Term Evolution Project of Reinforcement Learning[J]. arXiv preprint arXiv:2309.16382, 2023.

### Soundness
4

### Presentation
2

### Contribution
4

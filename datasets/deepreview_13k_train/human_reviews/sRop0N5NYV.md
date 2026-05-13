# Tactics of Robust Deep Reinforcement Learning with Randomized Smoothing

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
Despite randomized smoothing being proven to give a robustness guarantee, the standard performance of a smoothed deep reinforcement learning (DRL) agent exhibits a significant trade-off between its utility and robustness. Naively introducing randomized smoothing during the training or testing can fail completely in the DRL setting. To address this issue, we proposed new algorithms to train smoothed robust DRL agents while attaining superior clean reward, empirical robustness, and robustness guarantee in discrete and continuous action space. Our proposed DS-DQN and AS-PPO outperform prior state-of-the-art robustly-trained agents in robust reward by $1.6\times$ on average and exhibit strong guarantees that previous agents failed to achieve. Moreover, a stronger adversarial attack for smoothed DQN agents is proposed, which is $4.6\times$ more effective in decreasing the rewards compared to existing adversarial attacks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes new algorithms to train smoothed robust DRL agent and achieve good reward. Experimental results show that the algorithms outperform existing baselines. A new adversarial attach is also proposed and is shown to be more effective in decreasing agent rewards.

### Strengths
- The problem in consideration is interesting and timely.

### Weaknesses
 - It would be useful to explain how representative the issues in CROP are. Also, are there recent works that address/avoid these issues already? Fig.1 only compares results with CROP. It would be useful to have results from other methods.
- One issue I have is that the paper seems to contain two pieces of results, one for discrete and the other for continuous, and they seem to be quite orthogonal. It would be helpful to explain the common components of the schemes. 
- The baselines are all before 2022. Are there more recent methods? If so, please compare with them.

### Questions
- It would be useful to explain how representative the issues in CROP are. Also, are there recent works that address/avoid these issues already? Fig.1 only compares results with CROP. It would be useful to have results from other methods. 
- One issue I have is that the paper seems to contain two pieces of results, one for discrete and the other for continuous, and they seem to be quite orthogonal. It would be helpful to explain the common components of the schemes. 
- The baselines are all before 2022. Are there more recent methods? If so, please compare with them.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper tackles the challenge of enhancing the robustness of deep reinforcement learning (DRL) agents while preserving their utility. Although randomized smoothing offers robustness guarantees, its direct implementation in the DRL context often results in a trade-off between utility and robustness. To overcome this limitation, the authors introduce two innovative algorithms, DS-DQN and AS-PPO, tailored to train DRL agents that achieve high clean rewards and robustness certification in both discrete and continuous action spaces. DS-DQN and AS-PPO surpass previous robust DRL agents and introduce a more potent adversarial attack. Their contributions encompass addressing issues in prior methods, extending robustness guarantees to PPO settings, and introducing action bounds for continuous-action agents.

### Strengths
1. The paper's motivation, stemming from the shortcomings of existing smoothed agents and the trade-off between robustness and performance, is intriguing. The introduction of a robust guarantee sets this paper apart from mere proposals of simple robust RL training methods. It offers a deep understanding of RL robustness within the context of random smoothing.

2. The methods presented in this paper exhibit versatility by working across various types of tasks. The authors make commendable efforts to demonstrate empirical contributions on different domains, showcasing not only robust performance under empirical attacks but also robustness guarantees.

### Weaknesses
1. It would enhance clarity to use pseudocode diagrams to illustrate the algorithms' flow. Visual aids can make the presentation of the algorithms more accessible.

2. The experiment section suffers from suboptimal writing and presentation. The experimental results lack the strength of evidence needed to robustly support the claims made, and addressing this issue could significantly improve the paper's overall quality.

3. The paper falls short in the discussion of limitations. A more comprehensive exploration of potential limitations would provide a well-rounded view.

4. It's disappointing that the paper does not include ATLA[1] and WocaR-RL[2] as robust baselines. While the selected baselines do provide a reasonable basis for comparison, it is necessary and valuable to discuss these adversarial robust RL papers (as well as others that are not mentioned) in the related work section. I am concerned that the literature survey of robust RL baselines by the authors might not be comprehensive, especially with regard to recent works. (The authors do cite [1], but why do not discuss ATLA?)

5. Furthermore, I find the presentation of the experiments to be somewhat confusing. In Table 3, why is the comparison limited to SA-PPO and vanilla PPO, and where are Radial-PPO and other PPO-based baselines? It appears that the proposed method performs better only on larger attack budgets. However, in Table 8, it shows that AS-PPO does not have a significant advantage, or even any advantage, on large budgets.

6. In Table 5, the paper fails to clearly demonstrate the advantages of DS-DQN and AS-PPO; the terms "high" or "highest" are quite vague and do not provide an intuitive representation of contributions.

7. This paper introduces attack methods based on RS. However, the authors do not compare their attack method with the strongest evasion attacks, such as PA-AD[3], nor do they provide a discussion of prior attack methods in the related work.

### Questions
1. It's disappointing that the paper does not include ATLA[1] and WocaR-RL[2] as robust baselines. While the selected baselines do provide a reasonable basis for comparison, it is necessary and valuable to discuss these adversarial robust RL papers (as well as others that are not mentioned) in the related work section. I am concerned that the literature survey of robust RL baselines by the authors might not be comprehensive, especially with regard to recent works. (The authors do cite [1], but why do not discuss ATLA?)

2. Furthermore, I find the presentation of the experiments to be somewhat confusing. In Table 3, why is the comparison limited to SA-PPO and vanilla PPO, and where are Radial-PPO and other PPO-based baselines? It appears that the proposed method performs better only on larger attack budgets. However, in Table 8, it shows that AS-PPO does not have a significant advantage, or even any advantage, on large budgets. 

3. In Table 5, the paper fails to clearly demonstrate the advantages of DS-DQN and AS-PPO; the terms "high" or "highest" are quite vague and do not provide an intuitive representation of contributions.

4. This paper introduces attack methods based on RS. However, the authors do not compare their attack method with the strongest evasion attacks, such as PA-AD[3], nor do they provide a discussion of prior attack methods in the related work. 

[1]Robust Reinforcement Learning on State Observations with Learned Optimal Adversary. Huan Zhang, Hongge Chen, Duane Boning, Cho-Jui Hsieh. ICLR 2021.

[2]Efficient Adversarial Training without Attacking: Worst-Case-Aware Robust Reinforcement Learning. Yongyuan Liang, Yanchao Sun, Ruijie Zheng, Furong Huang. Neurips 2022.

[3]Who Is the Strongest Enemy? Towards Optimal and Efficient Evasion Attacks in Deep RL. Yanchao Sun, Ruijie Zheng, Yongyuan Liang, Furong Huang. ICLR 2022.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a smoothing method to find a trade-off between the robustness of the agent under adversarial attack and reward performance. In particular, it introduces two smoothed agents: DS-DQN for discrete actions and AS-PPO for continuous actions. The method is evaluated under different attack models and is compared with a previous method, CROP, and other baselines on three Atari games and three continuous control tasks.

### Strengths
- This paper tackles an important problem of learning robust policy in deep reinforcement learning setup.
- The empirical results seem better compared to the baseline on the tested environment.
- The methods appear to be easy to implement on top of existing algorithms (DQN, PPO).

### Weaknesses
 - The proposed method and its presentation rely heavily on the existing CROP method, thereby limiting its novelty.
- The method's description is dispersed throughout the paper, complicating comprehension, and the approaches for discrete and continuous cases appear to differ. Specifically, the use of a denoiser in the discrete case (DS-DQN) but not in the continuous case (AS-PPO) raises questions about the consistency of the approach. The description of the smoothing component in AS-PPO is also unclear.
- The implications of robust certification remain unclear within the context of the evaluated task. It's not clear how the certified radius and reward lower bounds are practically useful in the context of the Atari games or continuous control tasks. Furthermore, the connection between the theoretical guarantees and the empirical results is not well-established.

### Questions
What are the implications of a robust certificate in this context? How is it computed for experimental evaluation, such as for Atari Pong?
In DS-DQN, a random number generated from a Gaussian distribution is added to the state during training. A denoiser network is then employed to reconstruct the original state. Does this imply that, in an ideal scenario, the denoiser network essentially mirrors the Gaussian distribution introduced to the state initially? If so, what is the purpose of training such a denoiser when we already know the noise model added to the input? How does the denoiser contribute to achieving better rewards and enhanced robustness?

Is a denoiser model used for the continuous (AS-PPO) case? What constitutes the smoothing component in this PPO scenario? What does \Delta S_t represent in the paragraph following Equation 9?

I am not clear on why this denoiser method helps in achieving a better trade-off between robustness and reward. A detailed description would assist in understanding the empirical performance.

Are the attack models for discrete (DQN) and continuous (PPO) cases the same?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on CROP and an updated reward evaluation and defense metrics.

### Strengths
- This paper is clearly written and easy to follow.
- This paper targets a ‘mis’-evaluation in a past work: CROP, which is a clear motivation.

### Weaknesses
 - This work targets only on ONE random smoothing paper: CROP, which limits this paper’s signification. There is another concurrent work on random smoothing [1] with CROP. No discussion and comparison about [1] makes the contribution of this work unclear.
- This main concern the reviewer have is that this work is completely based on CROP and is a correction of CROP. Whether this paper should be published as a full research paper in ICLR main track is doubtful.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

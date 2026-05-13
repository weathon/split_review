# Ad-Hoc Human-AI Coordination Challenge

- Decision: Reject
- Scores: 5, 5, 6, 3

## Abstract
Achieving seamless coordination between AI agents and humans is crucial for real-world applications, yet it remains a significant open challenge. Hanabi is an established, fully cooperative benchmark environment that involves imperfect information, limited communication, theory of mind, and the necessity for coordination among agents to achieve a shared goal. These characteristics, in principle, make Hanabi an ideal testbed for exploring human-AI coordination. However, one key issue is that evaluation with human partners is both expensive and difficult to reproduce. To address this, we first develop \textit{human proxy agents} via a combination of behavioural cloning on a large-scale dataset of human game play and regularised reinforcement learning. These proxies serve as robust, cheap and reproducible human-like evaluation partners in our Ad-Hoc Human-AI Coordination Challenge (AH2AC2). To facilitate the exploration of methods that leverage \textit{limited amounts} of human data, we introduce a data-limited challenge setting, using 1,000 games, which we open-source. Finally, we present baseline results for both two-player and three-player Hanabi scenarios. These include zero-shot coordination methods, which do not utilise any human data, and methods that make use of the available human data combined with reinforcement learning. To prevent overfitting and ensure fair evaluation, we introduce an evaluation protocol that involves us hosting the proxy agents rather than publicly releasing them, and a public leaderboard for tracking the progress of the community. We make our code available as an anonymous repository: \url{https://anonymous.4open.science/r/ah2ac2-E451/}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
I acknowledge the rebuttal from the authors and and happy to rains my score.

 -------------------
This paper proposes a methodology for evaluating human-AI coordination in Hanabi using human-like proxy agents. The authors introduce the Ad-Hoc Human-AI Coordination Challenge (AH2AC2) with two sub-challenges that utilize limited amounts of human gameplay data (1,000 or 5,000 games). They contribute a new open-source Hanabi human gameplay dataset and baselines for both sub-challenges, including zero-shot coordination methods and methods leveraging the limited human data.

### Strengths
1.	The paper addresses the important issue of evaluating human-AI coordination in imperfect information settings.
2.	Conducting human proxy for evaluation is potentially valuable for ad-hoc teamwork.
3.	The release of a new Hanabi human gameplay dataset is a positive contribution.
4.	The challenge focusing on limited human data is relevant for real-world applications.

### Weaknesses
1. The core idea of employing behavioral cloning to create human-like agents in Hanabi builds upon previous work (Carroll et al., 2019), lacking significant innovation.
2.	The paper neglects to compare against more recent advancements in human-AI coordination for Hanabi and some interesting related works in overcooked.  
3.	While the human dataset and proxy models are a valuable contribution, the paper lacks a comprehensive analysis of the dataset's diversity and the strategies exhibited by the proxy agents. It would be beneficial to delve deeper into the dataset and compare it with existing analyses of human behavior in Hanabi.
4.	A demo website or interactive platform for the challenge would enhance accessibility and engagement with the community. Is it possible to release all datasets? If not, why? Can you release the pipeline of the dataset preprocess?

### Questions
see weakness

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes an Ad Hoc Human-AI Coordination Challenge (AH2AC2) to promote research on seamless coordination between AI agents and humans in the Hanabi benchmark environment. Recognizing the challenges of evaluation with human partners, the authors propose human agents using behavioral cloning based on a large human game dataset and reinforcement learning techniques. They introduce two data-limited challenge settings (1,000 and 5,000 games) to allow agents to exploit limited human data. To prevent overfitting, the authors adopt an evaluation protocol of hosted agents and maintain a public leaderboard for community tracking.

### Strengths
Originality: This paper addresses the important problem of human-AI coordination, which is a challenging and timely area for practical applications. Hanabi is a mature environment for exploring these dynamics, and AH2AC2 appears to bring structure to the field through a well-thought-out evaluation protocol.

Quality: The development of a human agent and the curation of a large-scale dataset of human Hanabi gameplay (over 10,000 games) demonstrate a significant amount of engineering effort and careful design for reproducibility. The provided public leaderboard adds value by creating a community-driven benchmark for progress.

Clarity: The paper is well-structured, with a clear description of each component, from the human agent to the baseline methods and evaluation protocols.

Significance: Human-AI coordination is a relevant problem, and the AH2AC2 challenge has the potential to be a useful testbed for researchers to evaluate methods in a reproducible manner without a human partner, thereby addressing a practical gap in the field.

### Weaknesses
Based on my understanding, this paper primarily serves as a benchmark paper, introducing a new benchmark based on a human dataset. However, several key weaknesses limit its impact:

	1.	Insufficient Analysis of Human Dataset and Proxy Agents: The paper lacks an in-depth analysis of the human dataset and human proxy agents. In Table 1, the authors provide only basic statistics (min, max, average, median, and standard deviation) for scores and game lengths. A more detailed exploration of the dataset, including aspects like trajectory, strategy diversity, and behavioral patterns, would greatly enhance the depth of the analysis and provide better insights into the proxies’ fidelity. For instance, analyzing the distribution of card plays, discards, and hints across different game states, or examining the frequency of specific sequences of actions, could reveal biases or limitations in the dataset and the resulting proxy agents. Furthermore, the paper does not explore the correlation between human player skill and the performance of the behavioral cloning agents, which is crucial for understanding the quality of the proxies.

	2.	Incomplete Introduction to the Challenge: The challenge setup is not thoroughly introduced, leaving the structure and implementation of the leaderboard unclear. Without this information, it is difficult to assess the challenge’s usability and rigor. The lack of leaderboard details also raises concerns that the development of the challenge may be incomplete. For example, are submissions evaluated on a held-out test set? What are the rules for submission? What is the frequency of evaluation? These details are essential for ensuring the integrity and reproducibility of the challenge.

	3.	Figure 3 is confusing, especially in the two-player setting, where the performance of all compositions appears similar. This could be due to multiple reasons—such as a highly effective dataset that results in nearly perfect models even using BC. However, this raises questions about the benchmark’s ability to differentiate between varying model qualities. Furthermore, it is unclear what the three-player setting represents and how it differs from the two-player configuration. The paper does not sufficiently explain why the three-player setting is included, nor does it discuss the complexities and strategic differences that arise in the three-player setting compared to the two-player setting, making it difficult to understand the value of this additional configuration.

	4.	Limited and Outdated Baselines: Given that this is a benchmark paper, the choice of baselines is crucial. The limited and outdated baselines evaluated here fail to showcase the challenge’s full potential. Including a broader range of up-to-date baselines would allow for a more comprehensive comparison and strengthen the benchmark’s value to the community. For example, the paper could have included more recent methods that combine reinforcement learning with imitation learning, or methods that explicitly model opponent behavior, which are more relevant to the human-AI coordination problem.

### Questions
See weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes to use Hanabi as an ad-hoc human-ai collaboration and sets up an evaluation methodology. The authors train behavior cloning (BC) / BC regularized agents of humans as a low-cost replacement for human players. The authors also promise a release of small subsets of human play data and host an online benchmark.

### Strengths
In general, I think the paper is well-written. Although using hanabi as a human-ai collaboration benchmark has been explored by several groups, I believe the effort promised in this paper will significantly contribute to the multi-agent ad hoc human-ai collaboration research.

### Weaknesses
I believe this paper lacks a justification/study on why the trained human proxy is a fair judge for this challenge.
(1) The bc policy, if not treated well in latent representation, eventually converges to a single average human policy. So BC+RL hypothetically stays around this average policy. One important aspect of collaborating humans in that human may demonstrate diverse collaboration conventions. Looking at Table 6, I wonder if with specific network mechanism to capture human behavior diversity will help the accuracy.

(2) As a human-ai benchmark, shouldn’t the qualitative/quantitative evaluation against real humans still be necessary for the public leaderboard? Then, you can compare the correlation between play with humans and play with human proxy. Otherwise, I believe the authors should spend more time justifying why human-proxy=human.

### Questions
See the question in weakness. 

(+1) How does the performance of BC/BC+RL trained on a small released subset compare to that of BC/BC+RL trained on the entire dataset, and what causes this difference? Is it due to the training not converging, or does it suggest a divergence in convention distributions between the two?

### Soundness
3

### Presentation
3

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
The paper is based on the Hanabi challenge, using human data to build evaluation partners and providing a benchmark along with a hosted evaluation platform to enable fair assessments.

### Strengths
The problem of ad hoc teamwork, which is closely related to human cooperation, is indeed worth attention, and Hanabi serves as an effective evaluation environment. I highly commend the authors for maintaining fairness by ensuring that evaluation partners are not public and are not solely determined by leaderboard rankings.

### Weaknesses
1. Low Effectiveness of Human Proxy

Ad hoc teamwork involves interacting with humans that the agents have never encountered before, posing a distributional shift generalization challenge, i.e, it is an special out-of-distribution challenge. Beyond the cost of collecting human data, the critical issue is whether the evaluation can reveal the algorithm’s ad hoc performance, i.e., whether the algorithm can maintain robust cooperation with a wide range deployment partners' policies.

Given that the human proxy is built through Behavior Cloning (BC) using limited human data, how can we ensure that these proxies introduce sufficiently diverse challenges? In other words, while the authors can guarantee that the human proxies are new partners (unseen during training), they cannot ensure diversity among these partners nor cover the full behavioral distribution of potential real-world human behaviors. This limitation weakens the validity of the evaluation.
I recommend referring to the following papers that discuss related issues: 

Wang, Xihuai, Shao Zhang, Wenhao Zhang, Wentao Dong, Jingxiao Chen, Ying Wen, and Weinan Zhang. "ZSC-Eval: An Evaluation Toolkit and Benchmark for Multi-agent Zero-shot Coordination." arXiv preprint arXiv:2310.05208 (2023).

2. Insufficient Baselines – Missing Comparison with State-of-the-Art Methods

The currently provided baselines are mostly simple extensions of self-play, such as IPPO, BC, HDR-IPPO, and BR-BC. These baselines are clearly insufficient. In the field of ad hoc teamwork, Zero-Shot Coordination (ZSC) is often regarded as a special case of the ad hoc teamwork problem. The authors should consider incorporating ZSC algorithms into the benchmark.

Li, Yang, Shao Zhang, Jichen Sun, Yali Du, Ying Wen, Xinbing Wang, and Wei Pan. "Cooperative open-ended learning framework for zero-shot coordination." In International Conference on Machine Learning, pp. 20470-20484. PMLR, 2023.

Zhao, Rui, Jinming Song, Yufeng Yuan, Haifeng Hu, Yang Gao, Yi Wu, Zhongqian Sun, and Wei Yang. "Maximum entropy population-based training for zero-shot human-ai coordination." In Proceedings of the AAAI Conference on Artificial Intelligence, vol. 37, no. 5, pp. 6145-6153. 2023.

Yu, Chao, Jiaxuan Gao, Weilin Liu, Botian Xu, Hao Tang, Jiaqi Yang, Yu Wang, and Yi Wu. "Learning zero-shot cooperation with humans, assuming humans are biased." arXiv preprint arXiv:2302.01605 (2023).

Yan, Xue, Jiaxian Guo, Xingzhou Lou, Jun Wang, Haifeng Zhang, and Yali Du. "An efficient end-to-end training approach for zero-shot human-AI coordination." Advances in Neural Information Processing Systems 36 (2024).

Strouse, D. J., Kevin McKee, Matt Botvinick, Edward Hughes, and Richard Everett. "Collaborating with humans without human data." Advances in Neural Information Processing Systems 34 (2021): 14502-14515.

3. Hanabi is a Great Environment but Not Sufficient

While Hanabi is an excellent environment, it alone is insufficient to represent the diversity of scenarios involved in ad hoc teamwork. Ad hoc teamwork spans multiple scenarios, and using only Hanabi as the environment is not enough. The authors should consider integrating additional cooperative environments, such as Overcooked or Google Research Football, to enhance the benchmark.

4. Discussion of Benchmark Results

The authors only demonstrate through experiments that the constructed human proxy agents can play Hanabi with different partner agents.
As a benchmark paper, the authors should further analyze the results to help the community understand what new insights this Hanabi-based benchmark brings to the problem of ad hoc teamwork. Currently, the discussion only demonstrates that the proposed approach can compute benchmark results. I do not see further insights or novel contributions from the authors regarding this issue.

### Questions
1. How can the diversity of the generated human proxy agents be ensured?
2. I don’t fully understand how cross-play can verify that the human proxy behaves similarly to humans. A score alone cannot adequately demonstrate behavioral similarity. I hope the authors can provide further explanation.

### Soundness
2

### Presentation
2

### Contribution
2

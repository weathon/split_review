# Emerging Safety Attack and Defense in Federated Instruction Tuning of Large Language Models

- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 6, 6, 3

## Abstract
Federated learning (FL) enables multiple parties to collaboratively fine-tune an large language model (LLM) without the need of direct data sharing.
  Ideally, by training on decentralized data that is aligned with human preferences and safety principles, federated instruction tuning can result in an LLM that could behave in a helpful and safe manner.
  In this paper, we for the first time reveal the vulnerability of safety alignment in FedIT by proposing a simple, stealthy, yet effective safety attack method.
  Specifically, the malicious clients could automatically generate attack data without involving manual efforts and attack the FedIT system by training their local LLMs on such attack data.
  Unfortunately, this proposed safety attack not only can compromise the safety alignment of LLM trained via FedIT, but also can not be effectively defended against by many existing FL defense methods.
  Targeting this, we further propose a post-hoc defense method, which could rely on a fully automated pipeline: generation of defense data and further fine-tuning of the LLM.
  Extensive experiments show that our safety attack method can significantly compromise the LLM's safety alignment (e.g., reduce safety rate by 70\%), which can not be effectively defended by existing defense methods (at most 4\% absolute improvement), while our safety defense method can significantly enhance the attacked LLM's safety alignment (at most 69\% absolute improvement).

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper addresses the vulnerabilities in the safety alignment of large language models (LLMs) trained through federated instruction tuning (FedIT). It introduces a novel safety attack method that allows malicious clients to compromise the safety of LLMs by using unaligned datasets, which can be generated automatically without human intervention. Meanwhile, this paper proposes a post-hoc defense method that involves the server generating aligned data to fine-tune the LLMs, thereby improving their safety alignment. Extensive experimental results demonstrate the effectiveness of the proposed attack and defense methods.

### Strengths
1. This paper for the first time reveals the vulnerability of safety alignment of LLMs trained via federated instruction tuning.

2. This paper proposes the first data poisoning method that aims to compromise the safety of FedIT.

3. This paper proposes a post-hoc defense method that effectively enhances the safety alignment of compromised LLMs.

### Weaknesses
*W1.* The attack model requires further clarification regarding the feasibility and necessity of data-based attacks. Typically, in FedIT, the attacker is assumed to be one of the parties who can control both the parameters transferred to the server and the training data. However, in this manuscript, the attacker is assumed to manipulate only the training data while leaving the local model parameters untouched. Additional explanation is needed on how this assumption aligns with real-world applications. Specifically, the claim that data-based attacks are more stealthy than model-based attacks needs rigorous justification. If data-based attacks are indeed more stealthy, it is unclear why the attacker would be constrained to only manipulating data and not the model parameters, as modifying parameters would likely be easier to implement and harder to detect. This assumption needs to be either removed or strongly supported with empirical evidence or theoretical analysis.

*W2.* The related work section lacks thorough comparisons. The manuscript claims to be the first work on data-based attacks, yet it is unclear when a data-based approach is preferable to a model-based one (see W1). Therefore, other attacks (both model-based and data-based) should be discussed and compared in the experiments. The manuscript needs to clarify what advantages data-based attacks have over model-based attacks in the context of federated instruction tuning. It is not sufficient to simply state that data-based attacks are more stealthy; this claim needs to be substantiated with experimental results or a detailed analysis of the attack vectors. The current discussion does not adequately address the existing literature on model-based attacks and their potential impact on FedIT.

*W3.* The experiments based on OpenFedLLM are not convincing. It is recommended to use more state-of-the-art or widely adopted LLMs for experimentation. Furthermore, stronger baselines, such as attacks that directly tune the parameters (see W1), should be included. The current experiments do not provide a comprehensive evaluation of the proposed method against the most relevant and challenging baselines. The choice of LLM and the limited set of baselines hinder the generalizability of the findings.

*W4.* There is limited technical challenge addressed in this manuscript. Simple fine-tuning with malicious or aligned data is applied without any specific techniques or novel approaches, providing limited insights for future research. The core idea of using malicious data to poison the model and then using aligned data to restore it is not novel. The manuscript needs to demonstrate a deeper technical contribution beyond applying existing techniques to a new setting. The technical challenge of addressing data heterogeneity in federated learning is not sufficiently explored.

### Questions
1. In the experimental setups, the paper claims that four benign datasets were considered. However, I have not found the experimental results of the Dromedary-verbose and Wizard-evol datasets.

2. This paper proposes a post-hoc defense to remedy the damage caused by attacks during FL. I wonder if existing centralized fine-tuning defenses [3] can mitigate the proposed attack? What is the innovation of this paper in the defense method?

3. I want to know the performance of the proposed attack on different proportions of malicious clients.

Reference

[3] Liu, Kang et al. Fine-pruning: Defending against backdooring attacks on deep neural networks. RAID’2018

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses attacks and defenses of safety alignment in federated instruction tuning. The authors propose a post-hoc defense method that fine-tunes the aggregated model with safe data at the server, thus restoring safety alignment without detecting malicious client models. Experiments demonstrate that the safety attack can significantly reduce the model’s safety rate, while the defense approach effectively restores the model's safety alignment.

### Strengths
1. This paper addresses safety alignment in federated instruction tuning, a problem that is both important and interesting. The authors propose attacks along with corresponding defenses to against the attacks.

2. The paper introduces a post-hoc defense mechanism that uses generated safe data to finetune the aggregated model and restore safety alignment without inspecting individual client models.

3. The authors conducted extensive experiments across multiple datasets and defense scenarios. The results show that the proposed attack can significantly compromise the model's alignment, while the defense method can restore alignment effectively.

### Weaknesses
1. The baseline defense methods used for comparison may not be well-suited to the attack in this paper. Methods like Krum, Median, and Trimmed Mean are designed primarily for Byzantine attacks that manipulate model weights, rather than poisoning local training datasets. Also, methods such as Foolsgold can be effective against backdoor attacks that might poison training data, e.g., label flipping attacks, but these methods were developed for classification tasks. However, this paper addresses text-generation tasks with different goals and attack mechanisms. Thus, I'm concerned about the relevance and effectiveness of these baseline methods.

2. The paper mentioned using a single NVIDIA RTX 3090 GPU to train models across 10 clients, with 3 clients participating training in each round. However, it's not clear how a single RTX 3090 can support fine-tuning three LLaMA2-7B simultaneously. Also, are the benign local models are trained with IID data?

3. The motivation for training LLMs with FL is unclear. While FL is primarily used to protect the privacy of local data, LLMs are often trained on publicly available datasets, which may reduce the need for privacy-preserving approaches in this context. I understand there may be sensitive scenarios, such as in medicine, law, or finance, where each FL participant wants to protect their data. However, these cases would involve different data distributions across FL clients, which are different from the experiment setting.

### Questions
Typically, applying defense mechanisms would lead to a reduction in accuracy. I'm curious if this also holds true for LMs. Since the approach involves using a different dataset for fine-tuning the aggregated model at the server, will this fine-tuning compromise the performance of the benign local models?

### Soundness
3

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
2

### Summary
This paper reveals that the current form of FedIT presents vulnerability when malicious clients train their local models with harmful datasets, resulting in compromised safety alignment of LLMs. While existing defense methods fail to address such attacks, this paper proposes a post-hoc defense by fine-tuning central LLM with harmless instructions and responses that are generated by external LLMs without any human efforts. The evaluation demonstrates the effectiveness of the proposed attack and improves the safety alignment of the proposed defense.

### Strengths
1. The paper explores the safety topic in federated learning, which is important to understand especially in the era of LLMs.

2. The paper is well-written and the logical flow of the paper is clear and easy to follow.  

3. The paper considers the scalability of the proposed work.

### Weaknesses
1. The authors should explain the assumption that malicious users’ objective is to make LLMs behave harmfully while given harmful instructions and behave normally when given normal instructions. 

2. The proposed attack is clear, yet the experiment setup (i.e., 30% are malicious users) is missing explanations.

3. The tradeoffs and benefits of the proposed defense method over existing defense methods need to be clarified. A clear comparison would have been helpful.

### Questions
Thank the authors for their work. Please see my questions as follows.

1. Could the authors clarify the rationale behind the attacker's objective of making LLMs behave harmfully only for harmful instructions? Have they considered scenarios where attackers aim to make LLMs behave harmfully for all types of instructions?

2. The authors assumed that 30% of users are malicious. The authors also stated for each round, only 3 out of 10 users were sampled. Is it randomly sampled? Moreover, for some rounds, users are all normal or malicious, which means this sampling process will naturally deal with malicious attacks. Could the authors provide a sensitivity analysis on the percentage of malicious users? Additionally, it would be valuable to see a breakdown of performance for rounds with different compositions of benign and malicious users to better understand the impact of the sampling process on the attack and defense effectiveness.



3. The authors performed most experiments on LLAMA-7B, and it is good to compare with other models. Could the authors provide hypotheses or analyses on why different models show varying levels of vulnerability to the proposed attack, as seen in Fig. 4? This could help in understanding if certain model architectures or training approaches are inherently more robust to such attacks.

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
This manuscript  presents a safety attack against federated instruction tuning (FedIT) along with a corresponding defense method. The focus is on data-based attacks, where the attacker (one of the parties) can manipulate the training data while adhering to the training protocol, without directly modifying the model parameters. The attack is performed using simple instruction tuning with a malicious dataset (obtained from either public or generated data). To defend against this attack, the authors propose fine-tuning with aligned data after training. The experiments show the propose method outperforms some baselines.

### Strengths
*S1.* This manuscript identifies vulnerabilities in FedIT caused by malicious data, which could compromise the alignment of large language models (LLMs).

### Weaknesses
*W1.* The attack model requires further clarification regarding the feasibility and necessity of data-based attacks. Typically, in FedIT, the attacker is assumed to be one of the parties who can control both the parameters transferred to the server and the training data. However, in this manuscript, the attacker is assumed to manipulate only the training data while leaving the local model parameters untouched. Additional explanation is needed on how this assumption aligns with real-world applications.

*W2.* The related work section lacks thorough comparisons. The manuscript claims to be the first work on data-based attacks, yet it is unclear when a data-based approach is preferable to a model-based one (see W1). Therefore, other attacks (both model-based and data-based) should be discussed and compared in the experiments.

*W3.* The experiments based on OpenFedLLM are not convincing. It is recommended to use more state-of-the-art or widely adopted LLMs for experimentation. Furthermore, stronger baselines, such as attacks that directly tune the parameters (see W1), should be included.

*W4.* There is limited technical challenge addressed in this manuscript. Simple fine-tuning with malicious or aligned data is applied without any specific techniques or novel approaches, providing limited insights for future research.

### Questions
N/A

### Soundness
2

### Presentation
2

### Contribution
1

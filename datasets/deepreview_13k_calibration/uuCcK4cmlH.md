# IDS-Agent: An LLM Agent for Explainable Intrusion Detection in IoT Networks

- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3

## Abstract
Emerging threats to IoT networks have accelerated the development of intrusion
detection systems (IDSs), characterized by a shift from traditional approaches
based on attack signatures or anomaly detection to approaches based on machine
learning (ML). However, current ML-based IDSs often lack result explanations
and struggle to address zero-day attacks due to their fixed output label space. In
this paper, we propose IDS-Agent, the first IDS based on an AI agent powered
by large language models (LLMs). For each input network traffic and a detection
request from the user, IDS-Agent predicts whether the traffic is benign or being
attacked, with an explanation of the prediction results. The workflow of IDS-Agent
involves iterative reasoning by a core LLM over the observation and action gen-
eration informed by the reasoning and retrieved knowledge. The action space of
IDS-Agent includes data extraction and preprocessing, classification, knowledge
retrieval, and results aggregation – these actions will be executed using abundant
tools, mostly specialized for IDS. Furthermore, the IDS-Agent is equipped with
a memory and knowledge base that retains information from current and pre-
vious sessions, along with IDS-related documents, enhancing its reasoning and
action generation capabilities. The system prompts of IDS-Agent can be easily
customized to adjust detection sensitivity or identify previously unknown types
of attacks. In our experiments, we demonstrate the strong detection capabilities
of IDS-Agent compared with ML-based IDSs and an IDS based on LLM with
prompt engineering. IDS-Agent outperforms these SOTA baselines on the ACI-IoT
and CIC-IoT benchmarks, with 0.97 and 0.75 detection F1 scores, respectively.
IDS-Agent also achieves a recall of 0.61 in detecting zero-day attacks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the authors propose an IDS-Agent to detect intrusions based on large language models (LLM). The pipeline of the proposed IDS-Agent is divided into multiple stages: data extraction, preprocessing, classification, and aggregation. The results show that IDS-Agent achieves F1 scores of 0.97 and 0.75 on the ACI-IoT and CIC-IoT datasets, respectively.

### Strengths
- The IDS-Agent is the first LLM agent designed specifically for intrusion detection.
- The author presents a clear pipeline regarding the design of IDS-Agent.

### Weaknesses
I appreciate that the authors clearly present the proposed method design and consider the use of the LLM agent for intrusion detection. However, this work has the following major weaknesses.
- The contribution of LLM in the proposed method is very limited. It seems that only in the aggregation-related stage, LLM shows a weak contribution compared to the traditional voting mechanism.
- In the experimental results (Table 1), Majority Vote achieves very close performance on the CIC-IoT 23 dataset and even higher performance on the ACI-IoT 23 dataset. Therefore, I am worried whether LLM for aggregation can work as the authors expect.

### Questions
I doubt whether the intrusion detection task really needs LLM to assist in the current way. Please refer to the weaknesses for rebuttal. I will check the related content carefully.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes IDS-Agent, the first LLM-powered agent for intrusion detection in IoT networks. IDS-Agent features capabilities for explanation, customization, and adaptation to various network attacks. It adopts a reasoning-followed-by-action pipeline, where the core LLM performs knowledge-enabled reasoning to decide the optimal tools for data extraction, preprocessing, classification, and results aggregation. Compared to existing ML-based IDSs, IDS-Agent achieves stronger detection performance and better interpretability by utilizing multiple ML models and external knowledge.

### Strengths
* IDS-Agent is the first LLM-powered agent for intrusion detection, with capabilities for explanation, customization, and zero-day attack detection
* It uses a reasoning-followed-by-action pipeline, where the core LLM decides the optimal tools for data processing and results aggregation, especially utilizing RAG for retrieving external knowledge
* IDS-Agent outperforms existing ML-based IDSs in detection accuracy and provides better interpretability; it can also effectively follow sensitivity instructions and detect zero-day attacks

### Weaknesses
 * The core detection capability of IDS-Agent still derives from the ML models in the toolbox; in other words, I think the main contribution of IDS-Agent is to propose a stronger ensemble method by utilizing LLMs and external knowledge (with RAG). However, due to some issues regarding the framework design (see Q1-4), it feels that the LLMs do not play a significant role in the process except for outputting human-understandable explanations by texts. As for the advantage of interpretability the authors claim, the final output does not give sufficient explanation as the readers might assume (see Q5). Besides, most of the components in IDS-Agent (pipeline, long-term memory, RAG) use existing approaches with no big changes specialized for this scenario. In general, the contribution of the paper might be reduced by these concerns.

* The paper does not include a comprehensive survey about related work in the field of network intrusion detection. A non-exhaustive list is below. Specifically, I recommend the authors survey not only AI-related conferences but also the big-4 security conferences. Accordingly, the evaluation will also be enhanced if IDS-Agent is compared to these SOTA methods specific to IDS rather than just general machine learning models.
  - ML/DL methods: [a-c]
  - Pretrained model methods: [d-f]
  - LLM methods: [g,h]

[a] Realtime Robust Malicious Traffic Detection via Frequency Domain Analysis, CCS 2022

[b] Detecting Unknown Encrypted Malicious Traffic in Real Time via Flow Interaction Graph Analysis, NDSS 2023

[c] HorusEye: Realtime IoT Malicious Traﬀic Detection Framework with Programmable Switches, USENIX Security 2023

[d] ET-BERT: A Contextualized Datagram Representation with Pre-training Transformers for Encrypted Traffic Classification, WWW 2022

[e] NetGPT: Generative Pretrained Transformer for Network Traffic, arxiv 2023

[f] Yet Another Traffic Classifier: A Masked Autoencoder Based Traffic Transformer with Multi-Level Flow Representation, AAAI 2023

[g] HuntGPT: Integrating Machine Learning-Based Anomaly Detection and Explainable AI with Large Language Models (LLMs), arxiv 2023

[h] ChatIDS: Explainable Cybersecurity Using Generative AI, arxiv 2023

* In addition to the comparative experiment, there are some other issues regarding the evaluation (see Q6-10).

* Minors:
  - page 2, line 66: (Shinn et al., 2023)) -> (Shinn et al., 2023)
  - page 4, Figure 1: Traffics -> Traffic

### Questions
1. When the LLM is reasoning, will it jump over any of the actions? According to my understanding, data extraction, data processing, and ML models are a must. If there are no variations, is there any difference between letting the LLM generate actions and writing a fixed program? As for KRM and LMM, I wonder about the proportion of the LLM that will trigger/jump over these actions, given the importance they seem to show in the ablation study.

2. Will the retrieved knowledge be inconsistent with the data type? For example, the retrieved knowledge of the ARP spoofing example you give in the paper might guide the model to pay attention to MAC addresses, while many datasets will not keep such environment-specific fields in order to prevent overfitting. If so, how will the knowledge help the final decision? (In fact, I appreciate the idea of using LLM-based RAG for expert knowledge retrieval, and I would like to see more contributions in this part)

3. The title of the paper is about IoT networks; however, I do not see clear intuitions or design points very specific to IoT networks over general networks. For example, [i] observes certain traffic patterns only in IoT networks and propose corresponding approaches. So I'm curious why IoT networks are mentioned in the headline.

4. In LTM, why timestamp is used? As the authors say, "the long-term memory base can be initialized by running the agent on a validation dataset", which will not correlate with the timestamps during the execution.

5. In the examples the authors give (Figures 1 and 2), I do not see very explicit "interpretability" as I expected: the LLM only analyzes the score distribution of the classification models and then makes the final decision, while typically the interpretability refers to the analysis of "what are the most important attributes to make such a decision" (see [j], and [g] combines LLMs with XAI techs). I particularly expect such a level of explanation as external knowledge is involved while there is not.

6. page 6, line 298: "... the IoT environment, which presents more complexities and challenges than traditional networks. " could the author explain this?

7. There are only two datasets used in the experiments. Usually, SOTA works in this field use much more datasets for evaluation, such as CIC-IDS 2017, CSE-CIC-IDS 2018,  UNSW-NB15. Even if the topic is limited to IoT networks, there are still datasets like BoT-IoT, ToN-IoT that focus on different IoT devices and attack types. 

8. page 6, line 305: "For evaluation, we construct a test dataset from the remaining samples in ACI-IoT’23 by randomly selecting 200 benign samples and 20 samples per attack category." Why only testing in such small sets? If it is because the API cost or qps limit, why not locally run some open-source LLMs like LLama?

9. I appreciate that the authors choose FAR as one of the metrics. However, the FAR of IDS-Agent is at a level of 3%-5%, while many SOTAs can achieve an FAR/FPR less than 1%. Note that benign traffic is much more than malicious traffic in reality, so in practice even an FAR of 1% will cause a flood of manual checks. I wonder how the authors address this issue.

10. Table 1: Basically, there is no big improvement between the performance of vanilla majority vote and IDS-Agent (especially when using GPT-3.5). This result again makes me feel it is the ensemble of multiple ML models that gives IDS-Agent primary detection capability, not the analysis of LLM. So I wonder if there will be more evaluation that can show my thought is wrong.

[i] Packet-Level Signatures for Smart Home Devices, NDSS 2020

[j] Interpreting Unsupervised Anomaly Detection in Security via Rule Extraction, NeurIPS 2023

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes an IDS Agent, a framework of LLM agents for network intrusion detection.

### Strengths
The paper is well-written and presents some good ideas on the hot topic of using LLM. The main contributions are zero-day threat detection and the ability to provide explainability over the decisions.

### Weaknesses
 * The paper's main contribution is the application of LLMs for IoT Networks, which seems contradictory given IoT’s focus on resource-constrained edge devices, where lightweight models, such as TinyML, are typically applied. Given these constraints, the authors should clarify the specific advantages of LLMs in this domain and provide practical examples to show how this approach can be beneficial.

* On Line 56, the authors state, _"particularly in safety-critical IoT scenarios where understanding the rationale behind alerts is crucial."_ The term “rationale” needs clarification: does it refer to interpretability, explainability, or something unique to IoT networks? Also, it’s unclear why understanding alert rationale is more critical in IoT scenarios than other network types. The authors should provide specific examples or cases illustrating why this distinction matters, particularly for IoT. Likewise, in Lines 297-299, the authors state that _"this paper focuses on intrusion detection in the IoT environment, which presents more complexities and challenges than traditional networks." _ The authors should enumerate and explain these challenges relative to traditional networks.

* In Lines 072-075, the authors describe a knowledge-based feature with long—and short-term memory components that resembles a traditional LSTM approach. While interesting, comparing this method with conventional LSTMs would help clarify its unique contributions. How does this approach differ from an LSTM regarding performance, and what benefits does it bring? The authors could consider discussing metrics such as speed, memory use, and interoperability to clarify why their proposal is preferable to a standard LSTM.

* “FlowID” is mentioned multiple times but lacks a formal definition. Since the definition of FlowID varies across sources, the authors should define it clearly to avoid ambiguity.

* The paper’s proposed method does not appear to operate in real-time, raising concerns about practical applicability. The authors should justify their choice of an offline approach that takes up to 8.65 seconds per instance for attack detection. For example, in a DDoS scenario, such a delay could result in extensive network downtime. The authors should discuss the potential impacts and outline the architectural and hardware challenges of implementing a real-time solution.

* The authors should specify which features were selected for each dataset and conduct a detailed analysis regarding preprocessing. In particular, they should indicate which attacks were included in training and testing sets. The apparent randomness of selection could mean that similar attack types (e.g., flood attacks) appear in both training and testing sets, potentially skewing results.

* In Lines 343-345, the authors mention constructing a knowledge base for IoT attacks using 50 online blogs and 50 research papers. It would be helpful if the authors could explain their criteria for selecting these sources to clarify the knowledge base’s reliability and relevance.

* The quantitative analysis section is underdeveloped. For example, further information on false classifications in the multi-class classification would help readers better understand where the model’s challenges lie.

* Additionally, in the quantitative analysis, the authors should benchmark their system against traditional IDS tools like Zeek, Suricata, and Snort. These rule-based systems are often effective against the standard attacks found in the datasets and could provide valuable points of comparison and complementary data sources for the proposed system. Additionally, discussing how LLM-enhanced IDS might complement these tools for a more comprehensive defense strategy would add depth.

* The zero-day attack analysis is somewhat confusing. The authors use ACGAN to generate CAN protocol samples, but the paper focuses on IoT networks. The relevance of comparing CAN protocol attacks with IoT-related attacks, like HTTP slow loris, is unclear. The authors should clarify how these two attack types are analogous or justify why this comparison is valid.

* In Lines 455-457, the authors state, _"We set the threshold as 0.7 in our experiments."_ A more thorough analysis of this threshold would be beneficial. A performance curve across varied thresholds could offer insights into sensitivity and precision adjustments.

* Additionally, the authors should consider comparing their proposal with traditional deep learning methods for zero-day attack detection. Since many deep learning (DL) models can perform attack detection in an unsupervised manner [1], such a comparison would contextualize the benefits of the proposed approach.

* The performance evaluation should be expanded. The appendix mentions an 8.65-second processing time per sample, but more detail is needed. A breakdown of processing times for each stage—preprocessing, analysis, information retrieval, and inference—would be beneficial. Furthermore, discussing how the system would perform in a real-world setting would provide important context.

### Questions
Minor comments:

* Line 072 has double parenthesis.  
* Line 168 in Figure 1 should be network traffic instead of "traffics" 
* Line 256 "STM" should be STR
* Line 918 Excution should be Execution.

### Soundness
2

### Presentation
2

### Contribution
2

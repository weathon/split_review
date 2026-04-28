# BlockFound: Customized blockchain foundation model for anomaly detection

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 5, 6, 6

## Abstract
We propose \sys, a customized foundation model for anomaly blockchain transaction detection. 
Unlike existing methods that rely on rule-based systems or directly apply off-the-shelf large language models, \sys introduces a series of customized designs to model the unique data structure of blockchain transactions. 
First, a blockchain transaction is multi-modal, containing blockchain-specific tokens, texts, and numbers. 
We design a modularized tokenizer to handle these multi-modal inputs, balancing the information across different modalities. 
Second, we design a customized mask language learning mechanism for pretraining with RoPE embedding and FlashAttention for handling longer sequences.
After training the foundation model, we further design a novel detection method for anomaly detection. 
Extensive evaluations on Ethereum and Solana transactions demonstrate \sys's exceptional capability in anomaly detection while maintaining a low false positive rate. 
Remarkably, \sys is the only method that successfully detects anomalous transactions on Solana with high accuracy, whereas all other approaches achieved very low or zero detection recall scores.
This work not only provides new foundation models for blockchain but also sets a new benchmark for applying LLMs in blockchain data.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes BlockFound, a customized foundation model for anomaly transaction detections in Blockchain. Traditional rule-based approaches and techniques relying on off-the-shelf language models struggle with generalizability and scalability. In order to address previous limitations, BlockFound leverages a multi-modal tokenizer to handle the transaction features along with a Bert-based architecture using mask language modeling (MLM) to reduce computational demands. The experiment results demonstrate BlockFound outperforms the baseline models by achieving higher accuracy with lower false positive rates.

### Strengths
- Clear justification for using multi-modal approach to process input Blockchain transactions.

- Comprehensive evaluation between BlockFound and baseline models with ablation studies for validating the effectiveness of the designs.

- The implementation of the model and data are open-sourced.

### Weaknesses
 - The definition of anomaly transactions is ambagious. 

- The size of malicious transaction data is limited.

- Potential redundancy in transaction data. Since contract templates (e.g., ERC-20 tokens) are wildly used in smart contract development, the dataset may contain duplicate transactions.

### Questions
I appreciate authors’ efforts in identifying anomaly transactions in Blockchain via machine learning-based techniques. The methodology is clear and the model design is persuasive in general, but I still have several concerns on the transaction data used in this manuscript along with questions for authors to respond.

## Q1: The definition of anomaly transactions is ambagious.
Since the blockchain transactions can vary wildly in structure and content, it would be helpful to have a clear definition of the anomaly transactions. From my understanding, there could be various kinds of transactions regarded as anomaly. For example, the transactions emitted by malicious users to trigger smart contract vulnerabilities either on the implementation level (e.g., integer overflow and reentrancy) or logic level (e.g., inappropriate access control to methods) can be one kind of anomaly transactions. The fraud/phishing transactions belong to another kind. Could the authors supplement a clear definition of the anomaly transactions studied in this paper?

## Q2: The size of malicious transaction data is limited.

I noticed that only 28 malicious transactions in total were used in the training/testing dataset, which is quite limited. I am concerned about if the model can effectively learn the features of anomaly transactions from such a small dataset. Could the authors justify how the proposed model can reliably learn and differentiate the benign and malicious transactions based on the imbalanced dataset?

## Q3: Potential redundancy in transaction data.

Contract templates are wildly used in real-world smart contract development, leading to different smart contracts may offering similar or even identical APIs to the users. This could cause potential duplication in the transaction data. I have two related questions for the authors:

- Q3.1: For the transactions calling to the same methods with different argument values, do they contribute the equally to model training, i.e., can they be considered as duplicate?

- Q3.2: If the above transactions are indeed duplicate, is it possible that similar redundant transactions are present in the dataset used for this study?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a deep-learning model for anomaly blockchain transaction detection. By designing a modularized tokenizer for blockchain-specific tokens, texts, and numbers in the transactions, the model handles these multi-modal inputs, balancing the information across different modalities. The model also adapts the RoBERT to train the foundation model with a mask language learning, and makes use of the encoder to detect anomaly transactions.
The evaluation of the model on a meticulously curated dataset demonstrates its potential for applications, showcasing practical applicability in specific environments.

### Strengths
1.The paper designs a novel tokenizer that deal with different types of multi-modal inputs in a transaction record, which capture the sematic in different fields effectively and shows some performance improvement;
2.The paper adopts BERT-like model and use
mask language modeling to train the foundation model rather than using GPT-style models, forming a lighter model architecture.
3.The paper evaluates the proposed model in real-world transaction data, and the results appear to be quite promising, especially on Solana with high accuracy.

### Weaknesses
1.Although the adapted foundation model shows some performance improvement with RoPE and FlashAttention, it represents a typical data mining method that has been extensively applied to various tasks, thus limiting its originality.

2.The authors rank all the addresses in transactions by frequency and retain the top 7,000 most frequent addresses. Obviously, some information is lost, and there is no guarantee that low-frequency addresses and transactions are necessarily benign. Furthermore, the impact of this threshold on the model's performance is not explored, and it is unclear if 7,000 is an optimal value, or if a different number of addresses would yield better results.

3.FlashAttention is a key module to handle long inputs in the foundation mode. However, there has been no experimental evidence that this approach has any impact on the accuracy or complexity of the model. The paper lacks a detailed analysis of how FlashAttention affects the model's performance, specifically in terms of training time, memory usage, and convergence speed, beyond the claim of handling long sequences.

4.There are several Embeddings as inRoBERT such as Position Embedding + Token Embedding and Segment Embedding. However, the authors does not describe how many embeddings are adopted and what is the difference between these embeddings used in their model and those we generally known in RoBERT. The paper should clarify whether all standard RoBERTa embeddings are used, or if any modifications were made, and why.

5.The authors should clarify why specific methods, such as RoBERT, were chosen for the framework since there are a number of other BERT-like models that can be used for the modelling of long sequences, such as ELECTRA. A comparative analysis against other similar models is needed to justify the choice of RoBERTa.

6.Some seem too subjective as no relevant cases or references were found, for example: “..these models cannot capture
the long-range dependencies and complex temporal dynamics inherent in transaction data, resulting sub-optimal modeling performance...” in Section I and "...using MLM can significantly reduce
the computational cost...." in Section III.B

### Questions
1.What is the time and space complexity of the proposed method, and how does FlashAttention affect it?

2.Are low-frequency addresses BENIGN? How well does the model work if low frequency addresses are retained?

3.Why does the model chose RoBERT as foundation model and not another model? 

4.In Tokenizer, all tokens share the same vocabulary, since unique hash addresses are individual tokens, how can the size of this vocabulary be controlled to make it available at all times?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents BlockFound, a foundational model customized for detecting anomalies in blockchain transactions. It utilizes a modular tokenizer to handle multimodal inputs and employs masked language learning, RoPE embeddings, and FlashAttention technology for processing long sequence data. Extensive evaluations of transaction data from Ethereum and Solana demonstrate BlockFound's exceptional capabilities in anomaly detection while maintaining a low false positive rate.

### Strengths
1. BlockFound is a foundational model tailored for detecting anomalies in blockchain transactions, designed to accommodate their unique data structures.
2. A modular tokenizer processes multimodal inputs—specific tokens, text, and numbers—enhancing the accuracy of transaction feature capture.
3. Utilizing masked language learning, RoPE embeddings, and FlashAttention, the model effectively handles long sequence data, improving its ability to process lengthy transaction records.
4. Experimental evaluations on Ethereum and Solana transactions show that BlockFound excels in anomaly detection, demonstrating high accuracy and low false positive rates.
5. Design for the DeFi environment, offering valuable detection methods to protect user assets and enhance the security of blockchain financial transactions.

### Weaknesses
1. The paper primarily conducts experimental evaluations on Ethereum and Solana networks, lacking validation of the model's generalization capability and adaptability. The selection of only these two platforms, while popular, does not sufficiently demonstrate the model's robustness across the diverse landscape of blockchain technologies. The paper needs to address how the model would perform on platforms with different consensus mechanisms, transaction structures, and smart contract languages.
2. The paper highlights the model's performance but lacks transparency in decision-making. Integrating tools could improve interpretability and enhance user trust. The black-box nature of the model makes it difficult to understand why certain transactions are flagged as anomalous, which is a significant limitation for practical deployment in security-sensitive environments. The paper should explore methods to provide insights into the model's reasoning, such as attention visualization or feature importance analysis.
3. The BlockFound model may need further adjustments to meet privacy standards. While the paper mentions using publicly available data, it does not discuss the potential for re-identification or the risks associated with analyzing transaction patterns. The paper should address the implications of using transaction data for anomaly detection and propose methods to mitigate privacy risks, especially in the context of evolving privacy regulations.

### Questions
1. How does fine-tuning the GPT-4 model using the API enhance its performance for the same tasks or domains?
2. Can the model's generalization capability be further validated on other blockchain platforms?
3. As the blockchain ecosystem evolves, new attack patterns and transaction types may emerge. Can the model adapt to these changes?
4. Does noise and inaccurate information in the data significantly impact the model's performance?
5. In handling blockchain transaction data, privacy protection is a crucial consideration. How does the article address and safeguard user privacy data?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces BlockFound, a customized foundation model designed for detecting anomalous blockchain transactions. It modifies BERT model by using RoPE embedding and FlashAttention to suit the characteristics of blockchain transactions. The performance of BlockFound is evaluated using real Ethereum and Solana transaction data, demonstrating its superiority on key performance metrics over baseline methods.

### Strengths
First, the idea of using a LLM to detect anomalous transactions in blockchain is innovative. 
Second, the authors have appropriately adapted the LLM for blockchain transaction data, and these modifications have been proven effective through ablation study. 
Third, the authors evaluated BlockFound using actual blockchain data, and the results demonstrate that BlockFound achieves better performance compared to baseline methods.

### Weaknesses
1. The introduction of this paper needs to sufficiently explain the motivation behind utilizing an LLM for detecting anomalous transactions in blockchain environments. It lacks evidence to support the claim that blockchain attacks are mainly due to anomalous transactions. Indeed, existing works have discussed that vulnerabilities in consensus protocols can lead to attacks authors mentioned, including double-spending attacks, even when transactions are valid and normal. From another perspective, even if anomalous transactions are detected, the paper does not provide evidence demonstrating that such detection can effectively prevent attacks. Additional references or evidence should be provided to justify the need for anomaly detection in blockchain transactions.
2. The paper needs to clearly define what is an anomalous transaction. The ground truth for such anomalies is not clear. Only with a known ground truth of anomalous transactions can we discuss whether "using the reconstruction errors as the metric for anomaly detection" is appropriate.
3. There is a need for more detailed analysis on the reliability of the datasets used (types, the number of training samples, the number of testing samples, etc.). For example, the statement "our Ethereum dataset consists of 3,383 benign transactions for training, 709 benign transactions for testing, and 10 malicious transactions. The data was collected from October 2020 to April 2023." raises questions. Does this imply there were only ten malicious transactions on Ethereum from October 2020 to April 2023, or were these ten selected by the authors? If selected, what were the criteria for their selection?
4. Why did the study use two different model architectures for different datasets? Does this indicate that the learning models for malicious transaction patterns lack transferability, necessitating the independent training of a model for each specific blockchain/dataset?
5. While the paper is clear and logically presented, it is more like a technical report than an academic paper.

### Questions
Please see weaknesses.

### Soundness
2

### Presentation
3

### Contribution
3

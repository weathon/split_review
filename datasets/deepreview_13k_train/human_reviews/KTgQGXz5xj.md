# Federated Granger Causality Learning For Interdependent Clients With State Space Representation

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Advanced sensors and IoT devices have improved the monitoring and control of complex industrial enterprises. They have also created an interdependent fabric of geographically distributed process operations (clients) across these enterprises. Granger causality is an effective approach to detect and quantify interdependencies by examining how the state of one client affects the states of others over time. Understanding these interdependencies helps capture how localized events, such as faults and disruptions, can propagate throughout the system, potentially leading to widespread operational impacts. However, the large volume and complexity of industrial data present significant challenges in effectively modeling these interdependencies. This paper develops a federated approach to learning Granger causality. We utilize a linear state space system framework that leverages low-dimensional state estimates to analyze interdependencies. This helps address bandwidth limitations and the computational burden commonly associated with centralized data processing. We propose augmenting the client models with the Granger causality information learned by the server through a Machine
Learning (ML) function. We examine the co-dependence between the augmented client and server models and reformulate the framework as a standalone ML algorithm providing conditions for its sublinear and linear convergence rates. We also study the convergence of the framework to a centralized oracle model. Moreover, we include a differential privacy analysis to ensure data security while preserving causal insights. Using synthetic data, we conduct comprehensive experiments to demonstrate the robustness of our approach to perturbations in causality, the scalability to the size of communication, number of clients, and the dimensions of raw data. We also evaluate the performance on two real-world industrial control system datasets by reporting the volume of data saved by decentralization.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper presents a method of Granger causality computation in a federated setting, where clients with individual measurements do not share their data with the server directly, and a federated learning mechanism is applied to estimate the causality. The advantage of this method is that it can significantly reduce the amount of data transfer. Theoretical analysis shows that this approach converges to a baseline centralized oracle. Some results from experiments are also shown from both synthetic and real-world datasets.

### Strengths
- The application of federated learning to Granger causality is interesting and unique. 
- The paper has nice theoretical analysis with some insights discussed. 
- The problem studied appears to be important for practical applications in the IoT domain.

### Weaknesses
 - As someone who is not an expert in Granger causality or Kalman filters, it is quite hard to follow the detailed steps of the proposed method and why it is designed in this way. 
- The proposed method seems to only work with Kalman filter based client models.
- It is difficult to understand the key message from the experimental results. There doesn't seem to be much comparison with baseline methods, except for Tables 4 and 7, where it is unclear how the loss values in Table 4 should be interpreted, e.g., which one is better?
- Related to federated learning, it is not very clear what is particularly unique compared to a standard federated learning algorithm that minimizes a generic finite-sum objective function.
- In Equations (1) and (2), why are there two losses that need to be considered separately and have different learning rates? Wouldn't it be possible to define an overall objective to combine both losses, as commonly done in federated learning literature?
- At line 250, `The server model is a ML tool whose predictions and labels are...` I don't understand what this sentence means. 
- At line 466, `Our method performed better than all three baselines mentioned in table 4.` I cannot tell from Table 4 why the proposed method performs better than the baselines. Which numbers in Table 4 should I look at and how should I compare the numbers?
- Some theorems are stated too informally, such as Theorem 6.2. I would expect to at least have a condition of $t\rightarrow \infty$ for this condition to hold. Also, what is the difference between $t$ and $k$ (e.g., in (1) and (2))?

### Questions
- The authors are strongly advised to provide some background knowledge on Granger causality and its connection to Kalman filters, which could be added to the appendix. 
- There should be a pseudocode with all the detailed steps of the proposed algorithm, for both the clients and the server. From the current description in the paper, it is quite hard to understand what exactly is being done. 
- Can the proposed method work beyond Kalman filter based models?
- In Section 3, it would be helpful to clarify the relationship the state matrix and the low dimensional states. In particular, how are the functions $f_c$, $f_a$ and $f_{ML}$ usually defined?
- In Figure 1 and also in the text description, what does a model mean in this context? It seems to be different from machine learning models (e.g., neural networks).
- It would be best to define the centralized model and $C_{mm}$ before Table 1, since they are mentioned in Table 1 and $C_{mm}$ is also mentioned in the text below it, but they are defined much later in the paper. 
- In Equations (1) and (2), why are there two losses that need to be considered separately and have different learning rates? Wouldn't it be possible to define an overall objective to combine both losses, as commonly done in federated learning literature?
- At line 250, `The server model is a ML tool whose predictions and labels are...` I don't understand what this sentence means. 
- At line 466, `Our method performed better than all three baselines mentioned in table 4.` I cannot tell from Table 4 why the proposed method performs better than the baselines. Which numbers in Table 4 should I look at and how should I compare the numbers?
- Some theorems are stated too informally, such as Theorem 6.2. I would expect to at least have a condition of $t\rightarrow \infty$ for this condition to hold. Also, what is the difference between $t$ and $k$ (e.g., in (1) and (2))?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper proposes a federated approach to learning Granger causality for a multi-client state space system.The convergence of the framework to a centralized oracle model is proved. Comprehensive experiments are conducted to demonstrate the robustness and scalability of this method.

### Strengths
This paper proposes a federated linear state space system framework with client augmentation and server model for clients to learn Granger causality information, facilitating a more accurate representation of cross-client causality. This method is innovative and inspirational. 

Theoretical guarantees are provided on the co-dependence of the augmented client and server model. Extensive experiments on both synthetic data and real-world datasets highlights the framework’s effectiveness in learning causality. 

I appreciate the author’s clear writing which is easy to follow.

### Weaknesses
1.	The authors could discuss the scalability of their method to larger and more complex datasets. It may help explain the further expansion of this approach.
2.	The limitations of the proposed method don't seem to be mentioned in the paper, which I think is a necessary discussion.
3.	It is not clear if the comparison is fair enough,i.e. more details about baselines need to be demonstrated.Authors can refer to question 2 lined below.
4.	The two salient characteristics of this ML function mentioned in 4.1 need to be explained in more detail.
5.	There should be more details about the proof in the paper.Listing more references or giving more steps for proof is helpful.For example,the proof of Proposition 5.3 can be discussed more.

### Questions
1.	To the best of your knowledge, is your method the first federated approach to learning Granger causality？Is there any other federated approach that can be compared to your model? 
2.	Baselines without client augmentation or the server model are mentioned in the experiments.I wonder that what parts of these baselines are similar to yours.For example, are there baseline methods without the server model but with client augmentation?If so, could you explain the parts of these methods that are relevant to your approach?
3.	Could you provide more related work on Distributed Kalman Filter in the last 5 years?
4.	I am not sure that whether this method is of value for further research.In other words,is it only effective in a particular scenario (Granger causality learning)?
5.	What are the possible limitations of this approach? Could you provide some ideas to address them in future work?

### Soundness
3

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
3

### Summary
The paper introduces a Federated Granger Causality Learning framework designed to analyze interdependencies among geographically distributed clients in industrial control systems. By leveraging a decentralized machine learning approach, the framework allows clients to maintain their own models while sharing only low-dimensional state information with a central server, overcoming the challenges of bandwidth limitations and computational burdens associated with centralized data processing. The authors establish convergence dependencies between server and client models with convergence rates. Empirical validation through experiments on synthetic and real-world datasets demonstrates the robustness, scalability, and communication efficiency of the approach, highlighting its ability to save data volume while effectively capturing operational interdependencies.

### Strengths
1. The paper presents a novel approach to learning Granger causality in a federated setting, which is a relatively underexplored area in the context of decentralized systems. 
2. The authors provide a detailed convergence analysis and establish conditions for sublinear and linear convergence rates.
3. The paper is well-structured and clearly written
4. The significance of this research lies in its potential impact on various industrial applications where understanding interdependencies is crucial for operational efficiency and fault management.

### Weaknesses
The paper does not include any analysis or experimental results of federated learning in non-IID settings which is an important aspect of FL. 
A detailed privacy analysis of the proposed method is missing which is very important in a federated setting.

### Questions
1. How does the proposed method perform in non-IID data distributions among various clients?
2. Can you provide a detailed privacy analysis of the proposed methods, and how do you plan to address this important aspect in the context of federated learning?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work presents a federated learning approach to detect Granger causality among geographically distributed industrial operations, addressing the challenges of large-scale, complex data. Using a linear state space system framework, it reduces bandwidth and computational demands by leveraging low-dimensional state estimates.

### Strengths
* The paper studied a fresh problem in the federated setup. 

*The presentation of the paper is solid and the results presented are of the interest to the community. 

*Although the paper studies a new problem that is unconventional to the people working on federated learning, the presentation of the paper makes it understandable to the general audience. 

*The results presented carry novelty. Also, the simulation section is solid covering various network settings.

### Weaknesses
The paper does not suffer from a clear weakness. Although there are some room for improvement:

1) Please read the paper and correct the typos. For example, there is extra space before the comma in line 75.

2) Please fix the typos in the paper. For example, line 329 refers to Theorem 5.5 but I think it should be Lemma 5.5.

3) Without clear explanation of the results of the theorems and lemmas it is a bit hard to clearly think about the results and appreciate them. Given the space limitation in the paper, I suggest that you add clear discussions about the results obtained in the main text in the appendix. In particular, more discussions about the "interpretation" of the theoretical results can be added in the appendix to help the reader to appreciate the results.

### Questions
Please refer to my comments above regarding suggestions to improve the paper.

### Soundness
4

### Presentation
3

### Contribution
4

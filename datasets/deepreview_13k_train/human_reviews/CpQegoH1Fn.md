# Human-in-the-loop Neural Networks: Human Knowledge Infusion

- Decision: Reject
- Scores: 5, 3, 5, 3

## Abstract
This study proposes a method for infusing human knowledge into neural networks.
The primary objective of this study is to build a mechanism that allows neural networks to learn not only from data but also from humans. This motivation is triggered by the fact that human knowledge, experience, personal preferences, and other subjective characteristics are not necessarily easy to mathematically formulate as structured data, hindering them from being learned by neural networks. This study is made possible by a neural network model with a two-dimensional topological hidden representation, Restricted Radial Basis Function (rRBF) network. In rRBF, the hidden layer's low dimensionality allows humans to visualize the internal representation of the neural network and thus intuitively understand its characteristics. In this study, the topological layer is further utilized to allow humans to organize it considering their subjective similarities criterion for the inputs. Hence, the infusion of human knowledge occurs during this process, which initializes the rRBF. The subsequent learning process of rRBF ensures that the infused knowledge is inherited during and after the learning process, thus generating a unique neural network that benefits from human knowledge. This study contributes to the new field of human-in-the-loop (HITL) AI, which aims to allow humans to participate constructively in AI's learning process or decision-making and define a new human-AI relationship.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a method of infusing human knowledge into neural networks with two-dimensional topological hidden representations called restricted Radial Basis Function Networks. The method has been tested in Alzheimer's image data.

### Strengths
- The idea is very good and novel and would be a good contribution to the community.
- The paper is well written, the idea is clear and the presentation is good.

### Weaknesses
 - Poor evaluation with limited experiments and even more limited comparisons. The proposed method is validated only in one medical dataset. I would suggest to test it against other datasets too. Regarding the comparisons I understand that this is more difficult but you need to figure out a good ablation study at least.
- The method is applied only on one neural network which is considered not black-box. I would highly recommend to apply it in other regular networks or at least try to generalize it.

### Questions
Why do you need the rRBF and you can't just do the experiments in a regular NN?
How does $\Lambda$ if instead of having the human input in the initialization you have it after the training? since you mentioned in the beginning of the paper that the infusion can be executed in two different stages of the neural network training.

The figures should be self-contained with better descriptions and with higher quality of the figure. For example Figure 7 looks unprofessional and not fit for this venue.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a novel method for infusing human knowledge into neural networks by constructing a Restricted Radial Basis Function (rRBF) network, which incorporates human knowledge, experience, and preferences into the initialization and retraining phases of the network. The paper demonstrates the application of this method in Alzheimer's disease detection and compares its performance to standard neural networks, with experimental results validating its feasibility. This research provides an innovative approach for human participation in the AI learning process, opening up new possibilities for human-AI interaction.

### Strengths
Innovative method：

The paper presents an innovative approach for directly infusing human knowledge into neural networks through a Restricted Radial Basis Function (rRBF) model, expanding traditional human-in-the-loop (HITL) methods.
Application to Alzheimer’s detection provides a meaningful, high-impact example of embedding human insights into healthcare AI.
Quality:

### Weaknesses
1. **Scope of Experiments**:

   The experiments focus on Alzheimer's disease detection using MRI data. However, the study would benefit from broader experimental validation across other tasks or datasets to assess the generalizability of the HITL rRBF approach. Applying this framework to different domains, especially those where data interpretation is less subjective, could help confirm the flexibility and robustness of the method. For instance, the method's performance on tabular data or time-series data, which lack the spatial structure of MRI images, remains unexplored. This lack of diversity in the experimental setup limits the conclusions that can be drawn about the method's applicability in different contexts.
   
2. **Baseline Comparisons**:

   Although the paper includes comparisons to non-HITL models, such as standard CNNs, it could be strengthened by including additional HITL benchmarks. For instance, other recent HITL approaches, or self-organizing map-based methods, could serve as complementary baselines. This would provide a more comprehensive assessment of how the proposed model stands in comparison to existing HITL techniques. Specifically, the paper lacks a comparison with methods that also leverage human input for model initialization or training, making it difficult to assess the relative advantage of the proposed rRBF approach. A more thorough comparison would involve methods that incorporate human feedback or guidance during the learning process, not just at initialization.

3. **Depth of Analysis on Human Knowledge Infusion**:

   While the paper demonstrates that human initialization improves model performance, the impact of specific types of human input (e.g., different expertise levels or subjective biases) is not explored in depth. Understanding how variations in human knowledge influence the model could clarify the boundaries and limitations of the infusion method, especially for practical deployment in diverse real-world applications. For example, the paper does not investigate how the model performs when the human input is noisy or inconsistent, which is a common occurrence in real-world scenarios. A sensitivity analysis on the quality and consistency of human input would be beneficial.

4. **Reproducibility and Scalability**:

   The paper states that the rRBF method relies on human organization of inputs, which raises questions about scalability for larger datasets. Addressing how the method could be adapted to datasets where human organization is not feasible, or discussing a hybrid approach combining human knowledge with automated processes, could enhance the method’s practicality. The paper does not provide a clear strategy for handling large datasets where manual organization of inputs becomes impractical. The method's reliance on manual input organization limits its applicability to scenarios where data volume is significant.

### Questions
no

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a method for directly infusing human knowledge into data-driven neural networks, based on the rRBF network, and attempts experimental validation. The authors named the hidden layer where human knowledge is infused as the Context-Relevant Self-Organizing Maps (CRSOM). This process can be executed both at the early or intermediate stages of the network's learning process. Experiments were conducted using an Alzheimer’s MRI dataset with six initializers participating. The results indicate that networks infused with human knowledge via the proposed method show the potential for superior performance compared to the baseline.

### Strengths
1. Infusing human knowledge into machine learning systems (or vice versa) remains an unresolved topic in the field of human-in-the-loop (HITL), and various approaches to address this challenge should be encouraged. This paper presents an attempt that can be positively evaluated in this regard. Although the study is limited to a classification problem, it could potentially be extended to broader applications, including reinforcement learning.

2. The mathematical formulation and flow in Sections 2.1 and 2.2 are relatively clear, which may benefit readers with diverse backgrounds.

3. Conducting experiments using complex, real-world medical imaging data is a reasonable approach, as it demonstrates the robustness of the proposed method.

4. The paper acknowledges its limitations explicitly in the introduction.

5. Despite the various weaknesses mentioned below, I believe this paper has considerable potential to be improved and developed more robustly in the future.

### Weaknesses
1. The authors state that the aim of this study is not to develop state-of-the-art models (Line 64). To acknowledge the contribution of this study, however, it is necessary to introduce a novel concept (an innovative methodology or rigorous human behavioral experiment results). These contributions, however, appear somewhat lacking. For example, the learning process of a network similar to SOM is known as a clustering process that corresponds to the high-dimensional space. If CRSOM identifies clusters that align with the arbitrary classified samples by the initializer, the authors' methodology could simply be considered a variant of SOM adapted to human prior knowledge (i.e., an application case).

2. As I understand only six subjects participated in the experiment. Given that the subjects were laypersons rather than experts, it is feasible to recruit more participants. However, with only six participants, it is difficult to ascertain the statistical significance of the experimental results.

3. For an experiment involving human subjects, it is necessary to describe the recruitment process, the participants’ characteristics, and whether IRB approval was required for the study, which is currently missing.

4. Even if it is accepted that expert involvement is not necessary at this stage of study, if non-experts evaluated MRI images for similarity, this judgment might not be substantially different from the similarity that an unsupervised learning model, such as an autoencoder, could learn. What if the autoencoder had instead learned and provided similarity information for these images that were then infused into CRSOM, rather than using human initializers? Given the domain of the experimental images, the general knowledge of non-experts could be within the range that the model could deduce independently. Thus, even if knowledge infusion is feasible, further examination may be needed to confirm whether the information infused was indeed uniquely human (i.e., unobtainable by the model itself).

5. There are several inaccuracies or omissions in the presentation. For instance, the figure legends tend to be insufficient. What does CROM refer to in Fig. 4? Is it CRSOM? Even if so, the explanation remains somewhat unclear. Personally, I suggest condensing Fig. 2 and Fig. 7 as they are somewhat disproportionate in size relative to the key information. Instead complementing the text to provide more detail on the human experimental procedures may be recommanded.

### Questions
1. The terms "re-learning" and "re-training" appear multiple times throughout the text. Do they have the same meaning? If so, is there a reason to differentiate them?

2. Although the objective of this study is not necessarily to propose a high-performance model, from a practical perspective, the proposed methodology underperforms compared to CNN. Would it not be more beneficial to integrate CRSOM into CNN and compare this with a baseline CNN instead?

3. In the main text, should Fig. 6 on line 315 be corrected to Fig. 5?

4. Overall, the figure legends are insufficient. Should the legend in Fig. 4 refer to CRSOM rather than CROM?

5. The legend in Fig. 7 lacks clarity. For example, a clearer term such as "rRBFs before the human corrections were made" could replace "learning."

6. While a "standard CNN" is mentioned, could you specify what is meant by a "standard CNN"?

7. With only six participants, does this study have sufficient statistical power?

8. Has ethical consideration been given to the use of human subjects in this experiment, including IRB approval?

9. In Fig. 3, what does "upper" precisely refer to? Does it represent a cognitive similarity metric as perceived by the initializer? If my understanding is correct, would it not be somewhat unnatural for perceived human similarities to appear as uniformly regular grid-like arrangements?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes a new method for infusing human knowledge into neural networks. It builds upon the Restricted Radial Basis Function (rRBF) network, similar to Self-Organizing Maps,   to infuse the knowledge by initializing the input based on human preferences. The proposed algorithm is evaluated on a brain MRI dataset for Alzheimer’s diagnosis.

### Strengths
• Infusing human knowledge in neural networks is a relevant topic , yet most studies focus on reinforcement learning, leaving other knowledge distillation techniques under-explored;

• The idea of mapping the input data to a new representation space respecting human preferences is interesting and novel;

• Alzheimer’s disease detection from brain MRI is still a challenge, especially in the early stage.

### Weaknesses
• The main idea of this paper – initializing a neural network using a new data representation based on human preferences – is unrelated to the specific network architecture. The authors focused this study on a single architecture (rRBF), arguing for better interpretability. Yet, all the results presented could have been generated using any kind of deep neural network (CNN, Transformer, MLP, etc.). For instance, Fig. 4 could have been generated using the internal representation of a network at various depths. As reported in Fig. 7, the performance of rRBF is quite low compared to a simple CNN, which could have been expected by its shallow architecture (2 layers). I do not understand why the authors made such a choice and I think it highly limits the current experimental setup used to validate the method. Showing the benefit of their method on different families of DNN would highly improve the experimental design.
      
• My second concern, as expected by the authors, is about the pool of human initializers used to judge image similarities. They are not medical doctors, and their personal opinion about the similarity between two brain MRIs is highly questionable. This is easily seen in Fig. 7 where the model’s performance is no better than a simple CNN when using human judgment for 5 over 6 individuals. I recommend using a pool of medical doctors to perform this task. In this case, it should be interesting to understand the inter-individual differences between image similarities as judged by this pool of doctors. 
      
• The authors only performed experiments on a small brain MRI dataset (235 subjects), although they claim a very broad method. Additionally, no statistical tests or cross-validation schemes were performed to evaluate and compare the models (e.g., in Fig. 7). I would first recommend using a much larger dataset (such as ADNI for Alzheimer’s disease) and studying harder tasks (e.g., diagnosing MCI vs AD vs Controls) to clearly show the benefit of using human knowledge in a real-life scenario.
      
• Section 2.1 (describing the rRBF architecture) is unclear and I had to read the original papers from (Hartono, 2015, 2020) to clearly understand all the technical details. Besides, as I mentioned previously, I think the exact architecture is irrelevant in the proposed method and it does not add novelty to the current work (e.g. Fig. 1 is not novel per se as it only describes an rRBF network). I would recommend shortening this section, moving technical details to the appendix and re-focusing on the actual novelty of this work (which is the human infusion technique in Section 2.2).

### Questions
• Related to my 1st point in the weaknesses, why did the authors choose specifically rRBF networks in this work over more classical networks (CNN…) ? 

• In section 2.2, you mentioned that you solved a linear Multidimensional Scaling (MDS) problem to map the input data to a new representation space. Did you consider non-linear MDS techniques (IsoMap [1], Laplacian Eigenmaps [2], etc…) ? 

•  In Fig.3, you show attention maps on a brain MRI that you obtained by solving the linear MDS problem on human judgments. They seem hard to interpret as very different areas are highlighted (frontal lobe, ventricles, etc…). Did you perform a statistical analysis to retain only the significant regions? A finer analysis would be interesting to compare the inter-individual differences between human annotators. 

[1] A global geometric framework for nonlinear dimensionality reduction, Tenenbaum et al., Science 2000
[2] Belkin, M., & Niyogi, P. (2003). Laplacian eigenmaps for dimensionality reduction and data representation, Belkin et al., Neural Computation, 2003

### Soundness
1

### Presentation
2

### Contribution
1

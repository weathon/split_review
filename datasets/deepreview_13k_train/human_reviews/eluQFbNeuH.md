# BetterBodies: Reinforcement Learning guided Diffusion for Antibody Sequence Design

- Decision: Reject
- Scores: 3, 5, 3

## Abstract
Antibodies offer great potential for the treatment of various diseases. However, the discovery of therapeutic antibodies through traditional wet lab methods is expensive and time-consuming. The use of generative models in designing antibodies therefore holds great promise, as it can reduce the time and resources required. Recently, the class of diffusion models has gained considerable traction for their ability to synthesize diverse and high-quality samples. In their basic form, however, they lack mechanisms to optimize for specific properties, such as binding affinity to an antigen. In contrast, the class of offline \gls{rl} methods has demonstrated strong performance in navigating large search spaces, including scenarios where frequent real-world interaction, such as interaction with a wet lab, is impractical.  Our novel method, BetterBodies, which combines Variational Autoencoders (VAEs) with \gls{rl} guided latent diffusion, is able to generate novel sets of antibody CDRH3 sequences from different data distributions. Using the \absolut simulator, we demonstrate the improved affinity of our novel sequences to the SARS-CoV spike receptor-binding domain. 
Furthermore, we reflect biophysical properties in the VAE latent space using a contrastive loss and add a novel Q-function based \filtering{} to enhance the affinity of generated sequences. 
In conclusion, methods such as ours have the potential to have great implications for real-world biological sequence design, where the generation of novel high-affinity binders is a cost-intensive endeavor.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the authors propose a framework to generate CDRH3 sequences with improved binding affinities to important receptors. In particular, the framework first pre-trains a variational autoencoder (VAE) to map each amino acid in CDRH3 sequences to a latent embedding. It then learns a diffusion model that sequentially generates these embeddings, which can be transformed back to amino acids, to construct the full CDRH3 sequences. To further improve the binding affinity, a Q function is trained to accurately estimate the Q-value for each action (i.e., each added amino acid), with previously added amino acids. This Q function is also used to guide the training of the diffusion model for better binding affinities. The experimental results show that the model can match or outperform the baseline.

### Strengths
* The method combines a VAE, a diffusion model, and reinforcement learning together to generate CDRH3 sequences.
* The method can match or outperform the baseline.

### Weaknesses
 * The formulated problem is relatively simple and may not require such a complex framework. In this paper, only CDRH3 sequences with 11 amino acids are considered, and variations in sequence length are not considered. With each amino acid having only 20 amino types, the search space, in the reviewer’s opinion, is limited. Given that specific motifs may exist at different positions in CDRH3, a combination of three complicated models may not be necessary for this task.

* It is suggested to include other state-of-the-art baselines for biological sequence design in the comparison. Currently, the paper uses only one baseline, which is not sufficient.

* It is suggested to clearly explain the design choices and do extensive ablation studies to validate them. For example, it would be helpful to validate the importance of the VAE latent space and the use of diffusion models in the overall framework.

### Questions
* The reviewer thinks this task is relatively simple. Given this simplicity, the reviewer thinks this complicated framework may not be necessary.  To validate the effectiveness of this framework, it is suggested that the authors add some simple search or optimization algorithms as baselines. For example, genetic algorithms, MCTS search algorithms, or even random policies, can also be used to generate novel CDRH3 sequences or mutate existing CDRH3 sequences for improved binding affinities. The reviewer wonders, within the same time constraints, whether these search or optimization algorithms can perform comparable or better than the proposed framework.

* The rationale for using a VAE to learn a two-dimensional latent vector for each amino acid is unclear. Given that the input sequence has a fixed length of 11, the reviewer thinks it is not necessary to learn additional embeddings for each amino acid. 

* The rationale for using a diffusion model to generate each amino acid also requires further explanation. The reviewer thinks that determining the amino acid type based on previously generated sequences is not a complicated problem, especially given the short length of sequences and limited number of amino acid types. 

 
* It is suggested that more baselines [1,2] need to be added for a comprehensive comparison.  Some related works [3, 4] for CDR3 sequences should also be discussed.

[1] Angermueller, Christof, et al. "Model-based reinforcement learning for biological sequence design." International conference on learning representations. 2019.

[2] Chen, Can, et al. "Bidirectional learning for offline model-based biological sequence design." International Conference on Machine Learning. PMLR, 2023.

[3] Chen, Ziqi, et al. "T-cell receptor optimization with reinforcement learning and mutation polices for precision immunotherapy." International Conference on Research in Computational Molecular Biology. Cham: Springer Nature Switzerland, 2023.'

[4] Karthikeyan, Dhuvarakesh, et al. "Conditional Generation of Antigen Specific T-cell Receptor Sequences." NeurIPS 2023 Generative AI and Biology (GenBio) Workshop.

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
4

### Summary
In this paper, the authors introduce BetterBodies, a method using variational autoencoders and reinforcement learning to generate antibody CDR H3 libraries. They use a VAE to compress amino acids to a two-dimensional latent space, grouped by physicochemical properties using a contrastive loss.

### Strengths
The paper engages with a complex and highly impactful problem setting: designing therapeutic antibodies.

### Weaknesses
The paper demonstrates a lack of awareness of both the practicalities of the problem at hand (ML-enabled antibody design) and the state-of-the-art in the field. Statements like “This [RL] is well suited to antibody sequence design, where direct access to a wet lab is not feasible” and “matches or outperforms the state-of-the-art method Generative Flow Network (GFlowNet)” reveal basic misunderstandings about the problem setting and state of the field. 
Developing methods for the offline setting using RL is not particularly relevant to real-world protein design, but is still of methodological interest and is interesting to explore, given contextualization with the broader field and the severe and impractical limitations of operating in an offline setting. There is already a rich literature in the online setting for protein and antibody design, which should be referenced and contrasted against. One such example is Li, Lin, et al. "Machine learning optimization of candidate antibody yields highly diverse sub-nanomolar affinity antibody libraries." Nature Communications 14.1 (2023): 3454. The main comparison is to GFlowNets, which is relevant insofar as the paper considers the offline RL setting, but the authors do not discuss or benchmark against any methods that are actually used in antibody design (i.e., methods that include wet lab validation). Antibodies are a leading class of drugs, but not only (or mainly) because of their binding properties.

### Questions
Can the authors provide sets of generated sequences and sequence-level evaluation beyond diversity and novelty to show their method is not simply reward hacking the Absolut! benchmark?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes BetterBodies, a framework that trains diffusion policy with RL to generate high-affinity CDRH3 sequences. They use the VAE to continuously represent the sequences and evaluate their results with Absolut! simulator.

### Strengths
The method itself is easy to understand and the use of diffusion models and RL is well-motivated.

### Weaknesses
This paper brings up several points worth considering:
- **Motivation**: The decision to use a 2-dimensional latent space in the VAE could be more clearly explained. While the authors suggest that combining VAE with contrastive learning can help group amino acids, it would be helpful to understand more specifically how this approach impacts model performance. Additionally, the rationale for a 2-dimensional space might benefit from further justification, as it may limit the ability to capture complex relationships. It seems that balancing high likelihood with predicted affinity might be possible using discrete diffusion alone, so more clarification on the essential role of the VAE component would be valuable.
- **Novelty**: The proposed method draws on a combination of existing techniques. A more detailed discussion on how these elements uniquely contribute to antibody design could enhance the sense of novelty.
- **Related Work**: Expanding the related work section to include notable antibody research from recent ML conferences (such as dWJS [1], AbODE [2], etc.) would strengthen the contextual foundation and illustrate the paper’s position within the field.
- **Experiment**: The experimental setup might benefit from including additional, recent baselines beyond GFlowNet [3], as several antibody-specific generative models have emerged in the past two years. Also, considering other evaluation tools like Rosetta or ML-based methods common in antibody research could provide more robust benchmarking. The Absolut! framework limits the evaluation to sequences of 11 residues, which might narrow the scope unnecessarily. Given these considerations, the current comparison could be enriched by including recent models or broader evaluation metrics.
- **Writing**: The clarity could be improved by refining certain sections for conciseness. For example, the discussion on diffusion models in the opening of Section 4 could be streamlined to maintain focus on the methodology itself.

### Questions
1. Could the authors clarify the necessity of the VAE component and the reasoning behind selecting a 2-dimensional latent space?
2. Given the mentioned limitations, what were the considerations for choosing Absolut! software for evaluation?
3. Is there a reason prominent antibody papers from recent ML conferences weren't cited or compared? Many of these also provide accessible open-source implementations.

### Soundness
1

### Presentation
2

### Contribution
1

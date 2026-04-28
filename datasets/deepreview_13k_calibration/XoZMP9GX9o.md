# Gumbel-Softmax Discretization Constraint,  Differentiable IDS Channel,  and an IDS-Correcting Code for DNA Storage

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 5, 3, 3

## Abstract
Insertion, deletion, and substitution (IDS) error-correcting codes have garnered increased attention 
    with recent advancements in DNA storage technology. 
    However, a universal method for designing IDS-correcting codes across varying channel settings 
    remains underexplored. 
    We present an autoencoder-based method, THEA-code, 
    aimed at efficiently generating IDS-correcting codes for complex IDS channels. 
    In the work, 
    a Gumbel-Softmax discretization constraint is proposed to discretize the features of the autoencoder, 
    and a simulated differentiable IDS channel is developed as a differentiable alternative for IDS operations. 
    These innovations facilitate the successful convergence of the autoencoder, 
    resulting in channel-customized IDS-correcting codes with commendable performance across complex IDS channels.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces THEA-Code: an autoencoder based method for designing error-correcting codes in DNA storage systems facing insertion, deletion, and substitution errors. In order to handle the difficulties brought by IDS channels with complex error patterns, the authors propose the two following key innovations: adding a Gumbel Softmax discretization constraint is to discretize the features of the autoencoder, and approximating the IDS channel with a differentiable transformer-based model.These techniques make it possible to generate tailored IDS-correcting codes that adapt to changing channel conditions, which provides better performance for DNA storage applications.

### Strengths
Novelty: The paper proposes a new method by introducing a Gumbel-Softmax discretization constraint into an autoencoder for IDS-correcting codes generation.

Quality: The proposed differentiable IDS channel is a new concept that will help to enable gradient based optimization in the presence of non differentiable IDS operations.

Significance: Tailoring error correcting codes for individual IDS channels will have substantial impacts on DNA storage technology, which involves coping with complicated error patterns.

Clarity: The paper is clear on the proposed methods and experimental setup, which allows understanding of contributions and results.

### Weaknesses
Evaluation Depth: The experimental results could be more thorough. Comparisons with existing methods are mentioned but not detailed, so it is hard to fully evaluate the relative performance.

Generalization: This manuscript only works with specific settings for the IDS channels. It will be more helpful if one can show that THEA Code performs well for a broader range of realistic DNA storage scenarios.

Ablation Studies: Some ablation studies are presented, but a deeper analysis on how different hyperparameters could affect the behavior of the model might give further insight into its behavior.

### Questions
Can the authors provide comparisons in more detail with existing IDS correcting codes, both combinatorial and heuristic, under the same experimental conditions?

How does THEA Code perform using real-world DNA sequencing data, which may have error patterns more diverse than those simulated?

Could this approach scale to larger sequences used in DNA storage more commonly, and what might be some of the challenges?

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
5

### Summary
This paper deals with coding for DNA storage. This problem is very popular in the research community as DNA based storage has a huge capacity. Sequencing operation is error prone and the errors which we can observe are not usual substitution errors but insertions and deletions. So, in order to deal with such errors new coding methods are required. Actually, such errors were already considered in the literature by Varshamov, Tenengoltz, Levenstein and others, these errors are a particular case of so-called asymmetric errors. But the problem is solved only for insertion or deletion of 1 symbol. The authors address the problem and propose new autoencoder-based codes that can deal with insertions, deletions and substitutions (IDS).

### Strengths
The main strong point are as follows:
- the authors propose to use end-to-end autoencoder-based solution as an as an IDS-correcting code 
- new differentiable channel model, called DIDS channel
- the use of Gumbel-Softmax for error-correcting coding task
- the final result is the code that can deal with IDS - to the best of my knowledge this is the first such code in the literature

### Weaknesses
I list the main weaknesses below:
- I would suggest to extend the section related to experiments and comparisons. The authors only present the results for their code for the error probability 1%. In this situation it is extremely difficult to understand how good the obtained codes are. What will change for larger error probabilities?
- «combinatorial codes (Cai et al., 2021; Gabrys et al., 2023) typically correct a single error rather than errors that can occur at multiple positions». But this is standard in error-correcting literature. E.g. BCH codes are designed to correct t errors but are applied in the channels with random errors. If the number of errors is greater than t you just declare a failure and take the received sequence as output.
- I would ask to make the comparison to classical combinatorial codes. E.g. there are VT codes that can deal with 1 deletion. Could you please compare you codes and VT codes in the channel with random deletions. I believe they will work fine for 1% deletion probability and length 150.
- Please provide some analysis of the THEA-Code, e.g. the distance (Levenstein distance). Also it would be beneficial to compare its cardinality with fundamental bounds from the literature (the capacity of deletion channel in not known but the bounds do exist).
- The usual problem for DNN-based decoding is the curse of dimensionality. In other words you cannot show all the codewords to the encoder/decoder. How did you solve the problem and how your decoder works on the codewords that were not shown to it during the training process?
- What is the purpose to introduce NER*?

### Questions
See weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This study explores a learning-based code design for the IDS channel. Given that the IDS channel is discrete, the authors first propose a differential IDS channel, using transformer-based models equipped with logical reasoning capabilities. Additionally, a Gumbel-softmax discretization constraint is applied to enhance the discreteness of the codewords.

### Strengths
The motivation for this work is clear, and its potential impact on the coding community could be substantial, as fully automated code/decoder design for discrete channels has not been extensively studied. The methods employed leverage recent advances, including transformer and Gumbel-softmax. Considering that practical DNA channels cannot be modeled with a rigorous mathematical framework, the ability to generate codes and decoders for arbitrary channels is highly meaningful and beneficial.

### Weaknesses
Despite the creativity and necessity of this approach, evaluating the effectiveness of this work remains challenging. While I understand the difficulty of comparing results with other studies in DNA coding, this work lacks any comparative analysis with prior research. The authors discuss an ablation study and provide simulation results, but there is no assessment of the proposed methods' effectiveness compared to other works. In the abstract, the performance of the proposed codes is described vaguely as "commendable." Although the automation ability is undoubtedly advantageous, a discussion on relative performance and complexity is essential, given that this research addresses a channel coding problem.

Below are several questions I have (most of them may be due to my own misunderstandings, and I would be grateful for clarification to aid readers who may struggle to understand as I have):
1. In figure 1, the probability vector C is shown to have a length of 5. Why, then, does the error profile have a length of 6?
2. The authors mention that the DIDS channel is implemented with a transformer-based model. It would be helpful to include the transformer-based model architecture for the DIDS channel in Figure 1, as there seems to be sufficient space to add it. Additionally, is the use of the transformer model essential, or merely effective? Would it be possible to employ other neural network architectures?
3. In Section 5.2, I am unclear about the reason for introducing auxiliary reconstruction. Although Section 6.3 demonstrates the necessity of this method through simulations, the motivation behind it remains unclear.
4. In Section 5.3, the authors mention that the encoder and decoder are also based on a transformer model. For the channel itself, using a transformer model might be acceptable, as the channel conditions are given in real-world applications, and thus the higher complexity of a transformer (relative to a typical neural network) is not problematic. However, for the encoder and decoder, using a transformer-based network could impose a significant complexity burden compared to the feed-forward neural networks commonly used in autoencoder research. Therefore, it would be beneficial to discuss whether a transformer model is strictly necessary for this purpose, and, if so, to provide an analysis of the associated complexity.
5. In Section 5.5, it appears that the codeword c is represented as a one-hot vector during testing, which could result in an excessively low code rate. However, based on Section 6, where the lengths of the source and codeword are given as 100 and 150, respectively, it seems that the codeword is not a one-hot vector. It would be helpful if the authors could clarify this. In Line 404, the codeword is described as "behaving like a one-hot vector," which led me to believe it was one-hot encoded.
6. What is the meaning of the color gradient in Figure 4? Does a darker color indicate a higher gradient? I am also struggling to interpret this figure. For example, does the "del(+3)" entry correspond to deletion at idx 0 (as mentioned in the caption)? If so, why does this imply a substitution at idx+3?
7. Table 2 presents experimental results for the Asc and Des channels. Why does the Asc channel exhibit better performance? Since Asc and Des channels are symmetric, shouldn't they achieve similar performance?

### Questions
Below are several questions I have (most of them may be due to my own misunderstandings, and I would be grateful for clarification to aid readers who may struggle to understand as I have):
1. In figure 1, the probability vector C is shown to have a length of 5. Why, then, does the error profile have a length of 6?
2. The authors mention that the DIDS channel is implemented with a transformer-based model. It would be helpful to include the transformer-based model architecture for the DIDS channel in Figure 1, as there seems to be sufficient space to add it. Additionally, is the use of the transformer model essential, or merely effective? Would it be possible to employ other neural network architectures?
3. In Section 5.2, I am unclear about the reason for introducing auxiliary reconstruction. Although Section 6.3 demonstrates the necessity of this method through simulations, the motivation behind it remains unclear.
4. In Section 5.3, the authors mention that the encoder and decoder are also based on a transformer model. For the channel itself, using a transformer model might be acceptable, as the channel conditions are given in real-world applications, and thus the higher complexity of a transformer (relative to a typical neural network) is not problematic. However, for the encoder and decoder, using a transformer-based network could impose a significant complexity burden compared to the feed-forward neural networks commonly used in autoencoder research. Therefore, it would be beneficial to discuss whether a transformer model is strictly necessary for this purpose, and, if so, to provide an analysis of the associated complexity.
5. In Section 5.5, it appears that the codeword c is represented as a one-hot vector during testing, which could result in an excessively low code rate. However, based on Section 6, where the lengths of the source and codeword are given as 100 and 150, respectively, it seems that the codeword is not a one-hot vector. It would be helpful if the authors could clarify this. In Line 404, the codeword is described as "behaving like a one-hot vector," which led me to believe it was one-hot encoded.
6. What is the meaning of the color gradient in Figure 4? Does a darker color indicate a higher gradient? I am also struggling to interpret this figure. For example, does the "del(+3)" entry correspond to deletion at idx 0 (as mentioned in the caption)? If so, why does this imply a substitution at idx+3?
7. Table 2 presents experimental results for the Asc and Des channels. Why does the Asc channel exhibit better performance? Since Asc and Des channels are symmetric, shouldn't they achieve similar performance?

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
5

### Summary
This paper investigates the use of Gumbel-Softmax as a discretization constraint within an autoencoder framework for designing insertion, deletion, and substitution (IDS) error-correcting codes, specifically targeting DNA data storage. Additionally, the paper presents a differentiable IDS channel that is designed to model the error patterns encountered in DNA storage, thus allowing the IDS-correcting code to be trained and tested under conditions mimicking IDS channels.

### Strengths
1. The paper explores Gumbel-Softmax as a discretization mechanism in a non-generative model, which is interesting.

2. The differentiable IDS channel is interesting as it allows learning IDS codes tailored to specific IDS channels.

### Weaknesses
While the paper proposes several contributions, they are somewhat loosely connected, giving the impression that they are brought together primarily to justify a full conference paper submission. The title of the paper, ``Gumbel-Softmax discretization constraint, differentiable IDS channel, and an IDS-correcting code for DNA storage,'' reflects this bundling.

The first contribution of using Gumbel-Softmax for discretization has some merit in itself but is not sufficiently substantial for a standalone publication (furthermore, I do not think that this contribution is entirely new, see Comment 3 below).

The remaining contributions focus on designing IDS-correcting codes for DNA storage. And in this sense, the paper is weak, showcasing notable limitations that impact its relevance and applicability in DNA storage.

Hence, in my opinion, the paper should be rejected. I motivate my decision in the following.

1. Lack of realistic DNA storage channel modeling: As the authors are aware, the literature on error correcting coding for DNA storage is extensive, and the paper rightly highlights the limitations of most works in this area (i.e., most works consider simplistic, unrealistic channel models). In this sense, designing error-correcting codes for a realistic DNA storage channel is both timely and relevant. However, this paper falls itself short of achieving this goal, i.e., it falls in the same trap (unrealistic channel models) that authors criticize.

Specifically, the authors overlook several recent works on error correcting codes for realistic DNA channel models, see, e.g., 

Maarouf et al., ``Concatenated codes for multiple reads of a DNA sequence,'' IEEE Trans. Inf. Theory, 2023.

B. Hamoum, et al., ``Channel model with memory for DNA data storage with nanopore sequencing,'' ISTC 2021.

Srinivasavaradhan et al, ``Trellis BMA: Coded trace reconstruction on IDS channels for DNA storage,'' ISIT 2021.

and

Welter et al, "An End-to-End Coding Scheme for DNA-Based Data Storage With Nanopore-Sequenced Reads," arXiv, June 2024.

Notably, the last two references include results for actual DNA synthesis and sequencing, and, to the best of my knowledge, the last paper presents most realistic DNA storage channel to date.

In this sense, a key limitation is that the paper does not address a realistic DNA storage channels, which should include multiple reads, non-iid errors, and strand-dependent errors.  Without these, the paper fails to demonstrate that the proposed IDS-correcting codes are applicable to DNA storage.

If the paper intends to target DNA storage applications, it is imperative to consider a realistic channel model. A realistic channel model (for Oxford nanopore sequencing, which is state-of-the-art) is described in:

Welter et al, "An End-to-End Coding Scheme for DNA-Based Data Storage With Nanopore-Sequenced Reads," arXiv, June 2024.

2. Absence of comparison with state-of-the-art codes: The paper does not compare the performance of the THEA-code against existing state-of-the-art IDS-correcting codes specifically designed for DNA storage. Without this comparison, it is difficult to assess whether the proposed codes achieve competitive performance (particularly for real-world DNA storage applications).

In particular, the authors should consider comparing the performance of their codes with the coding scheme in 

Welter et al, "An End-to-End Coding Scheme for DNA-Based Data Storage With Nanopore-Sequenced Reads," arXiv, June 2024.

and other existing schemes (see Figure 5 in the paper for references).

3. The analysis of the discretization effect of applying Gumbel-Softmax in a non-generative model is interesting. However, while I am not an expert in the topic, I am not sure that this is entirely new. In particular, the authors claim "it is found that applying Gumbel-Softmax in a non-generative model induces the categorical distribution to resemble a one-hot vector". It appears to me that this novelty is overstated

Indeed, I believe that this property was already known, see Jang et al. ``Categorical reparameterization with Gumbel-Softmax'' (see Figure 1, for example).

While the application of Gumbel-Softmax for IDS coding is new, the fundamental behavior of Gumbel-Softmax producing one-hot-like distributions in non-generative settings is not new.

### Questions
1. The authors should reword their experimental results section and compare the performance of their THEA-code to state-of-the-art ECCs for DNA storage. Without such a comparison, the relevance of this work is unclear.

2. In a realistic DNA storage channel, IDS errors are non-iid and are data-dependent. Can the differentiable IDS channel be extended to this setting?

### Soundness
3

### Presentation
3

### Contribution
2

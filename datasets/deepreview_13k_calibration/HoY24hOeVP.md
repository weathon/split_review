# Efficient Personalized Text-to-image Generation by Leveraging Textual Subspace

- Decision: Reject
- Avg Score: 5.40
- Scores: 6, 3, 6, 6, 6

## Abstract
Personalized text-to-image generation has attracted unprecedented attention in the recent few years due to its unique capability of generating  highly-personalized images via using the input concept dataset and novel textual prompt. However, previous methods solely focus on the performance of the reconstruction task, degrading its ability to combine with different textual prompt. Besides, optimizing in the high-dimensional embedding space usually leads to unnecessary time-consuming training process and slow convergence. To address these issues, we propose an efficient method to explore the target embedding in a textual subspace, drawing inspiration from the self-expressiveness property. Additionally, we propose an efficient selection strategy for determining the basis vectors of the textual subspace. The experimental evaluations demonstrate that the learned embedding can not only faithfully reconstruct input image, but also significantly improves its alignment with novel input textual prompt. Furthermore, we observe that optimizing in the textual subspace leads to an significant improvement of the robustness to the initial word, relaxing the constraint that requires users to input the most relevant initial word. Our method opens the door to more efficient representation learning for personalized text-to-image generation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a  method named as  BaTex for learning arbitrary embedding in a low-dimentional textual subspace. This paper also proposes an efficient selection strategy for determining the basis vectors of the textual subspace. The proposed methods achieve good performances on the public datasets.

### Strengths
This paper proposes a method named as BaTex for learning arbitrary embedding in a low-dimentional textual subspace, which is time-efficient and better preserves the text similarity of the learned embedding. The learned embeddings can not only faithfully reconstruct the input image, but also significantly improve its alignment with different textual prompt.

### Weaknesses
The novelty is limited. Although this paper proposes a method to extract the specific textual subspace for personalized text-to-image generation, the novelty of te proposed method is limited. The textual subspace vector is widely adopted for the conditional diffusion models, e.g. [Medical diffusion on a budget: textual inversion for medical image generation], [LaDI-VTON: Latent Diffusion Textual-Inversion Enhanced Virtual Try-On], etc. What's more, the pritority and advantages of the proposed method comparing with the traditional textual inversion is not obvious. The difference of the training step need to be clarified more clearly.

### Questions
1. Please highlight the priority and novelty of the proposed method from the whole diffusion procedures. 
2. Please add more analysis of the training details of the proposed methods comparing with the textual inversion.
3. Please add more experimental results of more conditions of the text-to-image tasks.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a method for learning embeddings in a low-dimensional textual subspace to achieve improved time efficiency and better preservation of text similarity in the learned embeddings for personalized text-to-image generation.

### Strengths
1. The writing is clear and easy to follow.

2. The authors propose using a reduced number of vectors to represent the original embedding, enabling the proposed model to undergo fewer training steps without significantly compromising performance.

3. The experiments presented in the paper support the authors' assertions. They require fewer training steps while achieving competitive performance compared to other methods.

### Weaknesses
1. I remain unconvinced regarding the claimed time efficiency of the proposed method. First, the paper only provides the number of training steps, but it lacks information on the actual time required for each step of the proposed method. Furthermore, the method's need for a loop to search for the proper number M, as shown in Algorithm 1, can be time-consuming. Specifically, the computational cost of determining the rank of the matrix $V_M$ at each iteration of the loop is not addressed. This rank computation, especially for high-dimensional embeddings, can be a significant overhead. Consequently, the quantitative comparison in Table 2 does not demonstrate a significant advantage of the proposed method.

2. I also have reservations about the qualitative performance of the proposed method. The paper showcases only a limited number of results with restricted diversity, such as a limited variety of style images. The lack of diverse examples makes it difficult to assess the robustness of the method across different styles and object types. For example, the paper does not demonstrate the method's ability to handle complex scenes or unusual object combinations, which are important for real-world applications.

3. I am unclear as to why the authors assert that previous methods solely focus on image reconstruction, thereby degrading their ability to combine the learned embeddings with different textual prompts. The primary objective of personalized text-to-image generation is to create new images based on input images. Additionally, Textual Inversion can also combine various textual prompts. The claim that Textual Inversion is inherently limited to image reconstruction and cannot effectively combine with different textual prompts is not adequately substantiated. The paper needs to provide a more detailed analysis of the limitations of existing methods in this regard, perhaps by showing specific examples where Textual Inversion fails to combine prompts effectively, while the proposed method succeeds.

### Questions
Please see above weaknesses. I am willing to change my rating if authors could address my concerns.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to address the issues of prompt editing degradation and time-consuming training process in personalized text-to-image generation.
To this end, it introduces an efficient method to explore the target embedding in a textual subspace with higher text similarity.
Specifically, it proposes a selection strategy to determine the basis vecors of textual subspace.
Experiments demonstrate that the learned embedding can both reconstruct input image and improve its alignment with editing prompts.

### Strengths
See summary.

### Weaknesses
1. The optimization of target embedding is performed in an explainable textual subspace. So could the authors provide visualizations of both learned weights and corresponding basis vectors (i.e., words)?
2. Too few methods are compared in this paper. The authors are encouraged to add more baselines including optimization-based [1] and encoder-based[2,3] in revision.
3. The expressiveness of words combination may be limited, especically in reconstructing image detalis, e.g., human faces.
4. The selection stratgy of textual subspace chooses M basis embeddings that are most similar to initialization embedding u. Is there too much redundancy among these basis embeddings?

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work primarily focuses on personalizing text-to-image models. The authors introduce Batex, a method that leverages multiple text embeddings with high similarity and updates their weights. This approach offers the advantages of reduced training time and improved text-image alignment. The paper provides both qualitative and quantitative results to support the effectiveness of the proposed method.

### Strengths
1. The organization and writing of the paper are commendable, resulting in a clear and easily understandable presentation.
2. The proposed method is both simple and effective, as exemplified by the compelling results presented in Table 2.

### Weaknesses
1. The authors say that their method offers advantages in terms of reduced training time and improved text-image alignment. However, the significance of improving training time may be less important considering the already inexpensive nature of personalization (text inversion). Additionally, the reasoning behind achieving higher text-image alignment compared to traditional text-to-image (TI) methods is not adequately clarified. Why TI cannot learn an embedding to align text and images? The claim that BaTex achieves better alignment needs more rigorous justification, especially given that TI methods are explicitly trained to align text and image embeddings. The paper should elaborate on the specific mechanisms within BaTex that lead to superior alignment compared to the inherent alignment capabilities of TI, and why those mechanisms are not already present or learnable in TI. 
2. It is hard to tell if Batex outperforms TI in Figure 2. It would be beneficial for the authors to provide further explanations regarding the superiority of Batex in Figure 2 to help readers better understand the comparative strengths of the proposed method. The visual differences are subtle, and the paper should provide a more detailed analysis of the specific aspects where BaTex excels over TI. For instance, are there specific attributes or details in the generated images that are better captured by BaTex, and if so, how can these differences be quantified or made more apparent to the reader?

### Questions
1. Pls see weakness.
2. How is the results of other baselines in fig 3?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In order to leverage a combined textual prompt and alleviate the computational demands of working in a high-dimensional embedding space, this paper introduces the BaTex method for acquiring versatile embeddings within a low-dimensional textual subspace for personalized text-to-image generation. The experimental results affirm the effectiveness of this approach.

### Strengths
1. The paper is excellently structured and offers a clear, comprehensible narrative.

2. This paper presents a novel approach, introducing textual subspace learning to eliminate the need for time-consuming training in high-dimensional embedding spaces.

3. The experiments provide compelling evidence of the efficiency and robustness of the proposed BaTex method.

### Weaknesses
1. Regarding the use of subspace learning:

Since the vocabulary V corresponds to a set of pre-trained vectors {v_i}, it might seem logical to directly select the top vector. So, this arises an important problem: why do we need to use the subspace learning method? Firstly, one important motivation is the combination with different textual prompts. I guess that this combination is implemented in a single subspace (and if my understanding is incorrect, kindly correct me). In Figure 2, it is not clear which textual prompts are amalgamated in this single subspace. Additionally, as depicted in Figure 3, the model considers multiple embeddings. Is the model simultaneously exploring multiple subspaces? Secondly, when we compare Figure 6 with Figure 8, we notice that both scenarios using the top vector manage to fulfill the textual descriptions. However, why does Figure 8 fall short in delivering the desired results? Specifically, in Figure 8, it's unclear why using only one basis vector leads to a significant degradation in image quality and fidelity compared to Figure 6, where multiple basis vectors are employed. The paper needs to elaborate on the specific mechanisms that cause this performance discrepancy. Furthermore, the relationship between the number of basis vectors and the quality of generated images requires a more thorough investigation and discussion.

2. Addressing missing objects in generated images:

Figure 2 highlights that the generated images miss some objects mentioned using the TI method. For instance, when examining the images from top to bottom, we notice the absence of objects such as a lady, a student, the beach, and a table. It's important to note that this work primarily focuses on learning a new embedding. How does this learned embedding enable the generation of missing objects? What is the mechanism for achieving this? The paper should clarify the specific aspects of the learned embedding that contribute to improved object generation. It is not sufficient to state that it improves text-to-image alignment; a detailed explanation of the underlying mechanics is necessary.

3. Clarification on optimization problem and loss:

In Equation (5), the optimization problem is to optimize the variable v. However, in Algorithm 2, the L_res loss is calculated concerning the variable w. Could you please provide clarification on this? The paper needs to explicitly state the relationship between *v* and *w* in the optimization process and provide a clear justification for using *w* in the loss calculation. The transition from optimizing *v* to optimizing *w* needs to be better motivated and explained in the context of subspace learning.

4. Discussion of limitations:

It appears that the paper lacks a discussion on its limitations. It would be valuable to address and discuss any limitations of this work. What potential constraints or drawbacks should readers be aware of when considering the findings and applications of this research? The absence of a limitations section is a significant oversight. The paper should address potential failure cases, computational costs, sensitivity to hyperparameter settings, and any other factors that might affect the practical applicability of the proposed method. This discussion is crucial for a balanced and comprehensive evaluation of the work.

### Questions
Please see the weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

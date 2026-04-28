# Extracting Symbolic Sequences from Visual Representations via Self-Supervised Learning

- Decision: Reject
- Avg Score: 4.20
- Scores: 5, 5, 5, 3, 3

## Abstract
In this paper, we explore the potential of abstracting complex visual information into discrete, structured symbolic sequences using self-supervised learning (SSL). Inspired by how language abstracts and organizes information to enable better reasoning and generalization, we propose a novel approach for generating symbolic representations from visual data. To learn these sequences, we extend the DINO framework to handle both visual and symbolic information. Initial experiments suggest that the generated symbolic sequences capture a meaningful level of abstraction, though further refinement is required. An advantage of our method is its interpretability: the sequences are produced by a decoder transformer using cross-attention, allowing attention maps to be linked to specific symbols and offering insight into how these representations correspond to image regions. This approach lays the foundation for creating interpretable symbolic representations with potential applications in high-level scene understanding.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose extending the DINO framework to handle both visual and symbolic information in order to generate symbolic representations from visual data.  Their approach learns structured symbolic sequences that capture the underlying compositional nature of visual data and is aimed at improving interpretability and visual reasoning tasks.

### Strengths
The paper is well motivated and the problem is important and strongly presented.  The writing is generally clear and easy to follow and the methods are evaluated clearly and against SOTA approaches.

### Weaknesses
Figure 2 should more explicitly point out which parts belong to the teacher and student models.  It would also help to have the figure match the description in 3.1 with explicit decoder, encoder and projector components labeled.

I am a little confused by the terminology and component descriptions in 3.1.  My understanding of the approach is that the student is trained as an auto-encoder that learns to encode continuous representations to discretized tokens.  The tokens are then converted to token representations that can be aligned with the original non-tokenized representation through a joint projection step.  Correct me if I am wrong.  I feel that the use of decoder and encoder in 3.1 is a little confusing as they are used differently to how I described above.  Perhaps cleaning it up as describing a decoder-encoder model that is aiming to learn a discretized decoding of the continuous latent space would be more clear.

On line 198, How does D_s discretize the latent?  This isn't clear in the next section either.

On line 235, how are the tokens defined?  This hasn't been covered yet.  This section is about selecting tokens in the discretization process but does not give an overview of what those tokens are or how they are computed.  If this is in prior work, it would be helpful to give a brief technical overview of the process used, with citations for the source of the approach, so the paper can be more self contained and reproducible.

Tables and results should include some measure of uncertainty to properly judge the significance of the results.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

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
This paper proposes a method for generating structured symbols from visual data based on abstract language.

### Strengths
The motivation of this article seems reasonable; however, the authors need to clarify this further in the discussion section, as there are many issues related to the core contributions.

### Weaknesses
 - The writing of this article is not clear, and there are significant problems with the experimental comparisons, lacking implementation and experimental details.
- The Teacher network is initialized with a ViT, and the attention structure of such self-supervised learning models fully has the capability to capture objects, as evidenced by the visualizations in many papers. Therefore, the images in Fig. 5 do not seem convincing.
- Additionally, most self-supervised visual models have the ability to discover representations. Similar to Fig. 5, I cannot understand what is special about the representation in this paper.

### Questions
What exactly is the symbolic sequence in this paper? Is it just a kind of VQVAE?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposed a novel self-supervised learning approach to extracting discrete and structured symbolic sequences from visual data. The core of this approach is a teacher-student framework, where the teacher provides pretrained visual features, and the student learns to convert visual features into symbolic sequences. The proposed model is trained on a variant of DINO loss, and the authors apply various strategies to enhance the generated symbolic sequences. The authors conduct experiments to visualize the region of symbolics, suggesting that the generated symbolic sequences capture a meaningful level of abstraction.

### Strengths
The main advantage of the proposed method is interpretability. The decoder transformer allows the attention maps to be linked to specific symbols, which indicates the regions these representations attend. This helps create interpretable symbolic representations, which can be applied to high-level scene understanding tasks.

### Weaknesses
1. This paper lacks details on model implementation and experimental setup, such as the structure of the encoder and decoder, and how the KNN and Linear Probing experiments were conducted. For example, the specific architecture of the encoder (e.g., number of layers, type of attention mechanism, dimensionality of the embeddings) is not provided. Similarly, the decoder's structure, including the number of transformer layers and the embedding dimension, is missing. The description of the KNN experiment should include the number of neighbors (k), the distance metric used, and how the visual features are used for the KNN search. For the Linear Probing experiments, the paper should specify the architecture of the linear classifier, the training procedure (e.g., optimizer, learning rate, number of epochs), and the evaluation metrics used.
2. This paper appears to lack important baseline models. All experiments only use different variants of the proposed method, without including other relevant models. For instance, the paper should compare against existing methods that extract symbolic representations from images, such as those using vector quantization or other discrete latent variable models. Without these comparisons, it is difficult to assess the novelty and effectiveness of the proposed approach.
3. In Fig. 2, the overview of the proposed approach is not clear. For instance, the figure does not illustrate which modules belong to the teacher models and which are the student models, and the projector is not shown in the teacher models. The figure should clearly delineate the teacher and student networks, including the flow of information between them. The projector, which is a crucial component for aligning the feature spaces, should be explicitly shown in the teacher network diagram. Furthermore, the figure should clarify how the visual features are processed before being fed into the student model.

### Questions
Could the authors provide test results of the proposed symbolic representations on high-level downstream tasks? Empirically, interpretable visual symbols could help address certain visual understanding tasks.

### Soundness
2

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
3

### Summary
The paper proposes a self-supervised learning method to learn visual symbolic representations. They use a teacher-student framework where the student predicts a discretised symbolic representation from source visual representations coming from a fixed teacher. The authors use attention masks used for predicted visual symbols to visualise what part of the image they activate on.

### Strengths
1. The motivation behind the approach and value of building systems that can extract symbolic representations from images is well presented.
2. The overall paper organisation is good (Although major issues in writing discussed below)

### Weaknesses
1. The experiments are very weak.
	* (a) The authors cite computational limitations but this work needs multiple datasets and even larger scale datasets for a decent validation of the approach.
	* (b) I am disappointed the authors do not experiment on any downstream tasks to illustrate the use of extracting symbolic representations. Some reasoning task (eg. VQA) or by-design interpretability via logical rules could be options. They will really drive home (1) the usefulness of visual symbolic representations, (2) that your method provides good quality of representations.
	* (c) There are no external baselines anywhere in the paper. I also wonder how the method would compare to a baseline if one simply learns a codebook by clustering DINO CLS token representations.
	* (d) No type of interpretability evaluation of attention masks. Some kind of segmentation or faithfulness evaluation should be possible. The authors should can check out the Quantus package for such metrics.

2. Throughout the system design and experiments, things are very poorly described, and are often unclear.
	* (a) The authors don't describe the system notations well. There are no notations for any input/output domains anywhere for any representation. At the bare minimum I'd expect you described dimensionality of your symbolic sequence/token (line 195, 201) but even that is not done. What is this teacher's joint distribution space "p"? Is it distribution of predicted class probabilities? Line 216 figure heading "KL Divergency" -> "KL Divergence".
	* (b) Table captions are barely descriptive. They do not describe what is inside the table. Even the main text is only marginally better at describing what is inside the tables. For instance in table 1, I do not understand what is the top-1, top-5 supposed to be for. Is it classification accuracy, which is what I am guessing right now? Is it accuracy for some underlying ground-truth set of human understandable concepts as lines 338-343 seem to indicate? The model abbreviations I assume are the different discretization strategies (should be clearly specified), but what is the number afterwards? Based on the paper I think it is the codebook size but nowhere in the whole section is this mentioned.  

### Questions
My questions asking for clarifications about writing are in Weaknesses 2(a), 2(b).

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes to abstract complex visual information into discrete, structured symbolic sequences using self-supervised learning (SSL). It extends the DINO framework to handle both visual and symbolic information. The method improves interpretability by linking the generated symbols to visual regions through attention maps.

### Strengths
1.	The paper focuses on an important and longstanding problem: extract symbolic information from complex visual input.
2.	The paper extend the DINO framework to handle both visual and symbolic information.

### Weaknesses
My main concerns are: lack of comparison with existing methods, and insufficient study about symbolic representations. The paper leverage several existing techniques (e.g., SSL, Vector Quantization), but it is confusing what is the new insight or discovery.

1.	Lack of comparison with existing methods. Tab.1 and Tab.2 are ablation studies about some strategy choices. However, how does the proposed model perform on image/video classification benchmarks? How is it compared with original DINO, or other SSL model without symbolic representation? 
2.	Few explorations of the advantage/necessity of symbol representations. The main claimed advantage is interpretability, i.e., several discrete feature maps in Fig.5. However, 
    - How can we use this interpretability in practice? Or, what are the conditions DINO feature fails to interpret? Since DINO feature has shown some emerging detection/segmentation ability.
    - How can the learned “symbols” benefit high-level scene understanding and abstract reasoning? The output feature maps are still complex and need human to summarize their meanings.

### Questions
My questions are listed in weakness section. My main concerns are performance comparison with existing SSL methods, and superiority of the proposed method.

### Soundness
2

### Presentation
3

### Contribution
2

# Hierarchically branched diffusion models leverage dataset structure for class-conditional generation

- Decision: Reject
- Scores: 6, 8, 5, 6

## Abstract
Class-labeled datasets, particularly those common in scientific domains, are rife with internal structure, yet current class-conditional diffusion models ignore these relationships and implicitly diffuse on all classes in a flat fashion. To leverage this structure, we propose hierarchically branched diffusion models as a novel framework for class-conditional generation. Branched diffusion models rely on the same diffusion process as traditional models, but learn reverse diffusion separately for each branch of a hierarchy. We highlight several advantages of branched diffusion models over the current state-of-the-art methods for class-conditional diffusion, including extension to novel classes in a continual-learning setting, a more sophisticated form of analogy-based conditional generation (i.e. transmutation), and a novel interpretability into the generation process. We extensively evaluate branched diffusion models on several benchmark and large real-world scientific datasets spanning many data modalities.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes hierarchically branched diffusion models for class-conditional generation. In a hierarchically branched diffusion model, branched points between all classes is generated based on the similarity between each class pair. The proposed model can be easily extended to continual learning scenarios. The model facilitates analogy-based conditional generation and provides a interpretability into the class-conditional generation process.

### Strengths
1. This paper is well-written and easy to understand.

2. The inclusion of well-crafted visualizations greatly enhances the comprehension of key concepts.

3. The proposed method offers meaningful advantages.

### Weaknesses
I did not find notable weaknesses of this paper.

A concern arises regarding the scalability of the proposed method as the number of classes increases. The experiments conducted appear to be limited to datasets with a small number of classes. It would be beneficial if the authors could present results for datasets with a larger number of classes.

### Questions
A concern arises regarding the scalability of the proposed method as the number of classes increases. The experiments conducted appear to be limited to datasets with a small number of classes. It would be beneficial if the authors could present results for datasets with a larger number of classes.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a method for class-conditional (label guided) sampling from a diffusion model by introducing branching. Analysis on several datasets suggests that the approach can be competitive (or perhaps even superior) in terms of generated sample quality. The proposed approach has several advantages compared to “classifier-free” guidance. It can readily incorporate new classes and can be used for transmutation (transferring a specific instance from one class to another). The method is considerably more efficient if the aim is multi-class sampling.

### Strengths
S1. The paper proposes a highly novel and elegant approach to class-conditional (label guided) sampling from a diffusion model. 
S2. Experiments indicate that the proposed method offers competitive (or better) performance to the state-of-the-art “classifier-free” guidance approach in terms of Frechet inception distance. 
S3. The paper details how the presented method can efficiently incorporate new classes without retraining the entire model and illustrates how the method can be employed for transmutation. Multi-class sampling is considerably more efficient compared to the state-of-the-art approach.  
S4. The paper is well-written and presents the proposed method clearly.

### Weaknesses
W1. Some of the experiments are not particularly compelling and serve more as examples of the potential of the technique rather than providing convincing evidence in support of the claims of the paper. In the image domain, analysis is limited to MNIST and the letter-recognition dataset; this leaves open the question as to how well the approach scales to other (less-structured) types of images and more challenging image classes, where the class hierarchy may not be so clear. 

W2. The branching point definition involves a threshold. There does not appear to be a concrete recipe for the selection of this threshold. Based on the paper it seems to be left to the practitioner to determine when branching points are “too close” to 0 or T. There is no investigation of how the selection of this threshold impacts performance. 

W3. Some of the claims in the paper are not adequately supported by experimental evidence. The claims should be moderated or experimental results provided to support the more general conclusions. 

The paper proposes a novel, intriguing and elegant approach. The major weakness of the paper is that most of the claims in the paper are supported by relatively limited experimentation. For example, the paper claims that the method achieves similar or better generative performance as the state-of-the-art, but does not clearly preface this with the clarification that the outperformance is observed only for two simple character-based image datasets and the similar performance is only established for one other dataset. The paper would be considerably more convincing if there were experiments on more challenging image datasets.

### Questions
Q1. “In general, the branched diffusion models achieved similar or better generative performance compared to the current state-of-the-art label-guided strategy. In many cases, the branched models outperformed the label-guided models, likely due to the multi-tasking architecture which can help limit inappropriate crosstalk between distinct classes.” – these sentences seem to be strong claims when the experiments are conducted on three datasets (two of which are similar). There seems to be no discernible outperformance for the single-cell RNA-seq data. The outperformance is really only for two character-based image datasets, so “In many cases” seems to be a stretch.  Considerably more extensive experiments on a variety of datasets are required to support the general claim made in the paper. Alternatively it could be restricted to “For experiments performed on two character-based datasets and an RNA-seq dataset, ….” 
Can the authors clarify whether they consider the current experiments to be sufficient to demonstrate similar or better generative performance? 

Q2. There are concerns that the Frechet inception distance can provide an incomplete or even misleading picture of generative quality (e.g., “The Role of Imagenet Classes in Frechet Inception Distance”, ICLR 2023; “Assessing Generative Models via Precision and Recall”, NeurIPS 2018). Do the authors consider that there would be value in employing other approaches for investigating sample quality?   

Q3. Why is the new class experiment limited to training on 3 classes? Is this to make the task easier? The new class experiment for the single-cell RNA-seq dataset seems to be similarly limited (just starting with two classes and adding a third). Is there a reason that the more obvious experiment of removing just one class and adding it back is avoided?  What happens if the “1” class is already included (i.e. something that is much closer to the introduced task)? 

Q4. “Of course, images and image-like data are the only modalities that suffer from this issue.” – why are images and image-like data the only modalities? Is there a “not” missing? Otherwise this seems to be an odd claim. The class-defining subject of a sequence could be at multiple parts of the image. The class of a graph can be defined by two subgraphs that are far from one another. 

Q5. “Additionally, this limitation on images may be avoided by diffusing in latent space.” – is there evidence for this claim?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a new way to do class-conditional generation in diffusion generative models by modelling the formation of class structures as a hierarchical ‘branching’-type process: The generation starts from a noisy image that contains no class information, and as generation progresses, the partially formed image starts narrowing down to a smaller set of classes. Whenever some classes are ruled, out this is denoted as a ‘branch point’. In the method, these points are empirically estimated from the noising forward process and the original training data, and during training and generation, a separate conditioning signal is given to each of the branches. Each class has a unique combination of branches. It is shown that this formulation of class-conditional generation helps in avoiding catastrophic forgetting in some scenarios, lends itself to novel image-translation-type conditional generation for MNIST, gene data and molecules. Additionally, the paper shows a method to visualize and interpret the branching points using averages of the noisy data points. There can also be a benefit in generation efficiency if sampling multiple classes by combining the generation of multiple classes at once.

### Strengths
+ The paper presents a creative use of the diffusion forward process itself for controlling the generation in a way that is mostly unexplored at the moment. 
+ The observation that training new classes on only subsets of the diffusion forward process avoids catastrophic forgetting, is particularly striking and seems like a genuinely new effect. Possibly this paper could be a first step towards utilizing this property in more realistic continual learning scenarios.
+ The paper also goes on to come up with different creative use-cases of the explicit branching structure, such as ‘transmutation’ where data points are transferred from one class to another using the branching structure, and in general finds multiple potentially relevant scientific data sets to experiment on. 
+ Perhaps the ideas here could inspire more research towards creating more structured diffusion generative models in the future.

### Weaknesses
 - Some of the experiments are not, at the moment, particularly convincing of the usefulness of the effects that they are showcasing. For the analogy-based generation with the RNA-seq data set, some marker genes were indeed changed, but do we have any other way to evalute the success of these generations? Could we formalize a clear objective on what does the conditional generation aim to do in the first place here? A similar issue exists for the molecule data set: Indeed regenerating does allow to generate cycled molecules from acyclic ones, but it is not clear what if any properties of the original molecule are retained this way. Just looking at the results, it seems possible that the generated molecules are a random mixture of the desired property and some atoms and bonds from the original molecules. 
- Continuing on the analogy-based generation, I feel that it would be appropriate to do an ablation where we use a regular diffusion model, noise out the data partially, and regenerate with the changed label. Would this work equally well, or differently somehow?
- The points about interpretability are also interesting, but it remains a bit unclear what could be the use of these average branching points.

### Questions
- What does the high correlation of expression between genes before and after transmutation mean here? That those particular genes often did not change? Is this the property that we want?
- Since adding uncorrelated noise probably does not result in clean hierarchical class structures in all cases (maybe in more complex image data sets, as pointed out in the paper), do you think it would be possible to induce such structure, e.g., by diffusing in some specifically designed latent spaces or otherwise designing the diffusion process itself to encourage it?
- I wonder if the example where catastrophic forgetting is avoided in MNIST is possible to extend to multiple steps, to a slightly more realistic continual learning scenario?

Overall, I think the idea is interesting and the paper presents new qualitative effects that emerge from the new formulation, but it is not there yet for publication. In particular, a more thorough experimental validation for continual learning and analogy-based generation would be in place, so that the reader would have clear takeaways. For the analogy-based generation, some kind of formalization of what are we targeting with the conditional generation, would also help with showcasing the potential significance.

### Soundness
3 good

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a novel framework for class-conditional generation using diffusion models, which are models that can generate realistic objects by reversing a noisy diffusion process. The framework called hierarchically branched diffusion models, leverages the hierarchical relationship between different classes in the dataset to learn the diffusion process in a branched manner. The framework has several advantages over existing methods, such as being easily extendable to new classes, enabling analogy-based conditional generation (i.e. transmutation), and offering interpretability into the generation process. The paper evaluates the framework on several benchmark and large real-world scientific datasets, spanning different data modalities (images, tabular data, and graphs).

### Strengths
* The paper addresses a novel and important problem of class-conditional generation using diffusion models, which can capture the rich information and structure of the data classes.
* The authors introduce a novel and flexible framework that can exploit the inherent hierarchy between distinct data classes by using branch points and can handle different types of diffusion models and paradigms.
* Extensive experiments and analysis are conducted to demonstrate the advantages of the proposed framework in continual learning, transmutation, and interpretability.

### Weaknesses
 * The paper is well-written, but some claims could be improved for clarification. For example, in Section 4 Page 6, it is unclear how the model performs with versus without fine-tuning the upstream branches that also diffuse over the newly added class in the continual learning setting without certain empirical results as support. Another example is that I found the observation in Section 5 Page 6 that letters with a larger feature value tended to transmute to letters with a larger feature value is hard to interpret from Figure 3b with only scatterplots of some feature values given.

* The efficiency of branched models over standard linear models when sampling multiple classes is clear from Table S9 when the number of classes is relatively small. Could the authors provide some insights when the number of classes grows very large with potential comparison regarding complexity analysis?

* In Figure 4, the interpretation at immediate branch points between two classes is shown and aligned with intuition. I am curious about how the visualization is for the branch point from more upstream such as the branch point between class 0 and the immediate branch point between class 4 and 9.

### Questions
* Why the FID between true and generated cells are the same for the branched and linear model in Figure S3 c)?

* Could the authors give some insights on why only one baseline of the label-guided (linear) models (Ho et al., 2021) is used for comparison?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

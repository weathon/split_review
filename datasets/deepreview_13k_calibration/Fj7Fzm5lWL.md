# Let's do the time-warp-attend: Learning topological invariants of dynamical systems

- Decision: Accept
- Avg Score: 5.25
- Scores: 6, 6, 3, 6

## Abstract
Dynamical systems across the sciences, from electrical circuits to ecological networks, undergo qualitative and often catastrophic changes in behavior, called bifurcations, when their underlying parameters cross a threshold. Existing methods predict oncoming catastrophes in individual systems but are primarily time-series-based and struggle both to categorize qualitative dynamical regimes across diverse systems and to generalize to real data. To address this challenge, we propose a data-driven, physically-informed deep-learning framework for classifying dynamical regimes and characterizing bifurcation boundaries based on the extraction of topologically invariant features. We focus on the paradigmatic case of the supercritical Hopf bifurcation, which is used to model periodic dynamics across a wide range of applications. Our convolutional attention method is trained with data augmentations that encourage the learning of topological invariants which can be used to detect bifurcation boundaries in unseen systems and to design models of biological systems like oscillatory gene regulatory networks. We further demonstrate our method's use in analyzing real data by recovering distinct proliferation and differentiation dynamics along pancreatic endocrinogenesis trajectory in gene expression space based on single-cell data. Our method provides valuable insights into the qualitative, long-term behavior of a wide range of dynamical systems, and can detect bifurcations or catastrophic transitions in large-scale physical and biological systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a method for classifying dynamical regimes in a data driven deep learning framework, combining a self-attention GAN for feature extraction and training an MLP for classification. 
Their main goal is to extract invariant topological properties from dynamical systems around bifurcations, and use them to classify dynamical regimes. To this end they leverage a data augmentation method, based on the principle of topological/dynamical equivalence. The first pre-train their model on variants of a simple oscillator system featuring a supercritical Hopf bifurcations.
They apply their pre-trained model to classify two regimes (pre-Hopf and post-Hopf) in several two-dimensional, autonomous systems (both synthetic and experimental data), featuring the same bifurcation. To this end they show that they can extend knowledge of dynamical classes (distinguishing between fixed point and cycles) across different datasets, and determine bifurcation boundaries and closeness to bifurcations.

### Strengths
The ideas in the paper are clearly presented. The idea of detecting bifurcations in dynamical systems is timely and important for applications. Their framework for data augmentation, based on the principle of dynamical/topological equivalence, is interesting, and the idea of transfer learning across different dynamical systems that share common topological properties seems like an important application. I also appreciate the application to experimental cell data, and the ablation studies in the supplement, investigating the effect of data augmentation and different modules, e.g. the attention modules, on outcomes.

### Weaknesses
Related Work/Dynamical Systems Theory:

One of my main concerns is that there is little reference to the rich mathematical body of work in dynamical systems theory anywhere in the paper. The concept of "dynamical equivalence" proposed in the supplement is well known in the literature (see e.g. Kutznetsov, "Elements of Applied Bifurcation Theory), as are the proofs given in 6.1. in the context of the concepts of topological conjugacy&topological equivalence. However, both terms are only mentioned once in passing in the whole paper, and as far as I could see are not referenced anywhere. The term "topological invariants", while used in the abstract and title, is also never formally introduced nor explained in the rest of the paper.

My second main concern is that I don't understand your reasoning why you "evaluate as baselines existing vector field representations, none of which explicitly encourage topological invariance". Topological features (such as fixed points, cycles, stability of fixed points etc.) can also be numerically approximated directly from the flow fields, especially for simple 2-D models you investigate here where the vector field is already present (i.e. fixed points are simply locations where the flow field is zero). There are other topological properties (e.g. persistent homologies, Betti numbers) that one could also extract to aid with classification.  At least using this as a baseline for comparison would seem crucial in the context of this paper? If I'm not completely mistaken this should at least work better than random guessing, as the comparison methods on the Selkov model effectively do. Fitting polynomial/other representations to the vector fields that a priori are not tailored to extract a useful representation for topological invariants seems perhaps unsurprisingly not so effective?
It could also be interesting in this context to investigate to what extent what your model extracts can be intepreted, and how it relates to other topological invariants.

Restriction to 2D

The restriction of all experiments to 2-D is also quite limiting. The authors indeed mention "technical challenges" in their conclusion for extensions to higher dimensions, but there are deeper theoretical reasons for these challenges, e.g. the lack of structural stability in higher dimensions, and more generally the scaling of your approach with the dimensionality of the dynamical system. Since this is a substantial limiting factor for extending your method to experimental settings, this could be made more explicit in the discussion.


In summary, in case I did not fundamentally misunderstand something about your approach and the general problem setting, it is unclear to me why you would need such a sophisticated machine learning architecture to extract features that can in the situation you investigate could be estimated from the flow directly? Since this is a crucial point to my mind point I am voting for rejection at this point, but am willing to adjust my score if these concerns are adressed.

### Questions
Your examples indicate that augmentation actually decreases performance for the simpler baseline models, which goes a little counter to the argument of your paper. Why do you think this is the case?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper introduces a method to identify the existence of fixed points and limit cycles in dynamical systems based on their vector fields in order to able to detect supercritical Hopf bifurcation boundaries. This method relies on a convolutional feed-forward network with attention and data augmentation that relies on warping. This method is then applied to some toy systems and single-cell data to identify different regimes in parameter space and differentiation transitions respectively.

### Strengths
This is to our knowledge the first method to perform topological invariant feature learning using deep learning.
The method has a high performance to detect bifurcation boundaries in various dynamical systems and even on real world data. Especially the application to detection of cell cycle score is a surprising contribution.
Furthermore, the effectiveness of the approach is demonstrated against a couple of other methods highlighting its applicability.
The paper is well written and present with a good flow to explain clearly the contributions. The particular contributions of the different parts of the network architecture and training method provides useful insights.  Robustness to relatively high levels of noise seem to further suggest the usefulness of this method for real world applications.
Identifying bifurcations is an important problem in dynamical systems theory and this paper shows some promising results to tackle it.

### Weaknesses
### weaknesses:
 \paragraph{Minor comments}
"In the left portion of Fig. ??" should have been "In the left portion of Fig. A7"?

The reference "ML Cartwbight. Balthazar van der Pol, 1960." seems erroneous.

\paragraph{Performance on systems that have both features}
It would greatly benefit the demonstration of the usefulness of the method, if there would be an assessment of the performance on systems that have both a fixed point and a limit cycle. Specifically, testing the trained model on samples of a subcritical Hopf bifurcation could reveal its capability to detect the monotonic relationship between class score and the order parameter, even if the system has not explicitly seen this bifurcation during training.

\paragraph{Figure 2}
It is surprising that the correlation coefficient for the BZ reaction is higher than Supercritical Hopf, while the boundary seems quite off. It would be beneficial to include a visualization of confidence as a function of the distance from the bifurcation boundary, along with Spearman's correlation, to better quantify the monotonic relationship.

\paragraph{Use of different training set sizes for the different methods}
The comparison of the method proposed in the paper to phase2vec and the Vector Field Learned Representation seem unfair considering that the models have been trained on a different number of training samples. Why is your model trained on 10K training samples why the others are trained on only 7.5K. This could explain why phase2vec is performing worse. A more equitable comparison would involve training all models on datasets of equal size. 

It would further clarify the differences between the methods if you could furthermore show how the inference of the bifurcation boundaries look like for the other methods. Specifically, including bifurcation boundary diagrams for each method would allow for a more direct visual comparison.

Finally, how do the other methods perform with the addition of noise? Benchmarking the performance of the baseline methods under various noise levels would provide a more comprehensive understanding of their robustness.

\paragraph{Use of the chosen hyperparameters}
The particular choice for the used hyperparameters is insufficient and makes the comparison to the other methods less convincing. For instance, the rationale behind using a learning rate of $10^{-4}$ and 20 epochs is not adequately justified. Showing the dependence of the performance of the methods on the different parameters would show how sensitive the method is to hyperparameter tuning. Specifically, reporting test accuracies across a range of learning rates and epoch iterations for each method would provide valuable insights into their stability and optimal configuration. Or stating that the best performing hyperparameters were chosen for each method would make the comparison better.

\paragraph{Comparison  to other methods}
To fully assess the contribution of this work a more extensive set of method to compare to should be considered. 
First, of all, Lyapunov exponents could be used to track bifurcations and the existence of limit cycles [1]. This method work for any dimension in principle, not just 2. A comparison of the sensitivity to noise between the proposed method and the Lyapunov exponent method would be particularly informative.

Furthermore, the Conley-Morse graph [2] should be considered. Is this method faster? More accurate than constructing the Conley-Morse graph or the method proposed in the paper? While the original Conley-Morse graph database assumes knowledge of the governing equations, adaptations for vector field representations could be explored. Additionally, investigating the computational complexity of the Conley-Morse graph in higher dimensions would be beneficial.

Finally, one could track down bifurcations through continuation algorithms [3]. The authors should clarify how their method addresses scenarios where parameter space is not accessible, and only isolated measurements are available, which is a common challenge in practical data science.

The performance of these other reliable methods would give a better idea of the usefulness of the proposed method.

### questions:
 Why was a learning rate of $10^{-4}$ chosen for training? Why 20 epochs? How was it "confirmed" that that "was enough to fit the training data"? Why were 20 coefficients used for the Fitted Parameter Coefficients? What is the justification for using a polynomial representation of degree 3 for the fitted parameter coefficients?

What is the discontinuity of the theoretical boundary in Figure 3 and Figure A12 relating to? Is it a result of the discretized computation of the boundary, and if so, how is the grid of alpha values determined?

How are cells partitioned into batches of at least 50 cells? How is the size furthermore determined for each batch? Does the partitioning have any consequences for the resulting model? Specifically, how does the batch size affect the resulting 2D grids, and what is the rationale behind the chosen minimal batch size of 50?

### Questions
Why was a learning rate of $10^{-4}$ chosen for training? Why 20 epochs? How was it "confirmed" that that "was enough to fit the training data"? Why were 20 coefficients used for the Fitted Parameter Coefficients?


What is the discontinuity of the theoretical boundary in Figure 3 and Figure A12 relating to?

How are cells partitioned into batches of at least 50 cells? How is the size furthermore determined for each batch? Does the partitioning have any consequences for the resulting model?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Authors propose a data-driven, physically-informed deep-learning framework for classifying dynamical regimes and characterizing bifurcation boundaries based on the extraction of topologically invariant features. Authors further demonstrate the method's use in analyzing real data, recovering distinct proliferation and differentiation dynamics along pancreatic endocrinogenesis trajectory in gene expression space based on single-cell data.

### Strengths
1. The experiments are extensive. 
2. The related works are well organized.

### Weaknesses
1. The paper is written poorly and hard to read. I cannot find the problem definition. What's the meaning of prototypical system? 
2. The main method is based on convolutional attention method and data augmentation, which is widely used in dynamical system modeling.
3. The methodology part needs to be reorganized. Authors should divide that into different parts, which can be related to the contributions. Now, it only shows data augmentation and an existing network to me.   
4. More SOTA methods should be compared. For example, there are extensive RNA velocity methods [1].

### Questions
See above.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors present a deep-learning framework designed for the classification of dynamical regimes and the characterization of bifurcation boundaries. Their approach is rooted in the extraction of topologically invariant features. The effectiveness of this method is convincingly demonstrated through its application to real-world data. Notably, the framework excels in the analysis of such data, successfully delineating distinct proliferation and differentiation dynamics along the pancreatic endocrinogenesis trajectory within the gene expression space.

### Strengths
- The paper introduces a novel approach to topologically invariant feature learning in dynamical systems, utilizing warped vector field data as augmentations to generalize across systems with similar dynamics in their topological representations within phase space. The method seems novel to me.
- The paper demonstrates the effectiveness of the proposed method through its application to real data, successfully recovering distinct proliferation and differentiation dynamics within the gene expression space of the pancreatic endocrinogenesis trajectory. This suggests a broad range of applications across various fields, including biology, physics, and beyond.
- The paper holds promise for making a substantial impact in the field of machine learning for dynamical systems, offering a new approach to addressing the challenge of predicting impending catastrophes in diverse real-world systems.
- The paper also suggests promising future research directions, including expanding the scope of invariance types and enhancing equivalence notions.

### Weaknesses
 - The methodology section appears disorganized. The addition of more subtitles would greatly enhance readability. Moreover, the frequent transition between the main content and the appendix disrupts the reading experience.
- The model setup details being located in the appendix can make it less accessible, as it's separated from the primary content.
- While the wording and sentences in the experiments section are well-constructed, there's room for improvement in the organization of tables and figures. Consider enlarging figures and addressing font size issues, particularly in tables. For instance, Table 3's column headers could be better aligned with their respective columns.
- The process for reproducing the results remains unclear. It would be beneficial to include a dedicated "Reproducibility Statement" section, providing readers with the necessary guidance to replicate the findings.

### Questions
In addition to the points mentioned in the 'Weaknesses' section, several questions arise:

- Regarding the model setup, it would be valuable to understand why the current configuration is deemed the most suitable for this problem. An ablation study, exploring architectural variations such as layers with different sizes, would provide insights into the model's design choices.
- Are there specific hyperparameters within this method that require tuning, and if so, what is the recommended approach for hyperparameter optimization?
- A dedicated 'Limitations' section would be a useful addition to provide a comprehensive perspective on the constraints and challenges of the proposed approach."

### Soundness
3 good

### Presentation
2 fair

### Contribution
4 excellent

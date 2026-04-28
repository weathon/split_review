# Differentiable and Learnable Wireless Simulation with Geometric Transformers

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
Modelling the propagation of electromagnetic wireless signals is critical for designing modern communication systems. Wireless ray tracing simulators model signal propagation based on the 3D geometry and other scene parameters, but
their accuracy is fundamentally limited by underlying modelling assumptions and correctness of parameters.  In this work, we introduce \wgatr, a fully-learnable neural simulation surrogate designed to predict the channel observations based on scene primitives (\egc surface mesh, antenna position and orientation). Recognizing the inherently geometric nature of these primitives, \wgatr leverages an equivariant Geometric Algebra Transformer that operates on a tokenizer specifically tailored for wireless simulation. We evaluate our approach on a range of tasks (\iec signal strength and delay spread prediction, receiver localization, and geometry reconstruction) and find that \wgatr is accurate, fast, sample-efficient, and robust to symmetry-induced transformations. Remarkably, we find our results also translate well to the real world: \wgatr demonstrates more than 35\% lower error than hybrid techniques, and 70\% lower error than a calibrated wireless tracer.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper presents a learnable approach to tackle the problem of indoor wireless simulation. The proposed architecture is based on a Geometric Algebra Transformer, and a new tokenizer is introduced, allowing to leverage a 3D representation of the scene by taking 3D primitives as input. The model can also be integrated into an inverse problem framework based on diffusion, allowing to retrieve the position of the transmitter, the receiver or the geometry of the scene. Two new datasets for wireless simulation are also presented. Experiments are conducted in synthetic and real settings.

### Strengths
- The presentation is clear and the paper is well-written. The problem at hand and coresponding challenges are well introduced to the reader.
- The quantitative and qualitative results show the superiority of the method in multiple settings, and with regards to multiple variables (number of training samples, number of training rooms / transmitters, etc..
- The versatility of the model is underlined by its adaptation to the inverse problem setting.

### Weaknesses
 - Although the results on synthetic data are convincing regarding the contribution of the proposed architecture, the impact of the proposed architecture w.r.t. the transformer is not so clear on real data, although the authors explain this by the simplicity of the scene. It is not clear if the geometric algebra transformer provides a significant advantage over a standard transformer when the scene geometry is relatively simple and lacks complex variations. The experiments on real data should perhaps include a more diverse set of environments to better assess the true benefit of the proposed geometric approach.
- The most competitive baseline (SEGNN) is not evaluated on the WiPTR dataset. This makes it difficult to fully assess the performance of the proposed method against the state-of-the-art, especially in more complex real-world scenarios. The absence of this comparison leaves a gap in the evaluation, as the SEGNN might perform better than the transformer baseline on this dataset, and it is unclear how the proposed method would compare.


### Questions
- Why does data augmentation lead to poorer results in some cases in table 2 for the transformer baseline ?
- Are the input coordinates of the transmitter/receiver 2D or 3D for the proposed model ?
- For Rx interpolation in in-distributions experiments (l. ~329) in table 1, have the floor layouts been seen by the model during training ? If so, this should be explained more clearly, and why this setting is relevant.

Minor remarks:
- l. 297: |ap|^2 -> ap^2 ?
- l. 315: while -> While
- l. 789: The The -> The

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors introduce Wi-GATr, a fully learnable neural simulation surrogate designed to predict wireless channels based on indoor scene elements, including surface mesh, antenna position, and orientation. They employ an equivariant Geometric Algebra Transformer with a tokenizer for wireless simulation. The proposed method is validated using two distinct simulated datasets.

### Strengths
(1) Wireless channel prediction is essential in wireless systems, and developing a fully learnable neural simulation surrogate for predicting wireless channels is an emerging topic.

(2) The techniques and experimental results in this paper are solid. The authors apply their proposed model not only to channel prediction but also to two inverse problems: receiver localization and scenario generation. Various simulation results further validate the effectiveness of the proposed method.

(3) The authors have developed two new 3D wireless datasets to validate their model, which would be valuable resources for the wireless research community if published.

### Weaknesses
(1) The novelty of this paper in the machine learning component is unclear. The core of the method seems to rely on applying an existing equivariant Geometric Algebra Transformer, and it's not evident what specific modifications or novelties are introduced within the transformer architecture itself or its training procedure for the wireless channel prediction task. The paper should clearly articulate the novel aspects of their approach beyond the application of a known architecture.

(2) The definitions of inverse problems lack clarity. The receiver localization problem, for instance, needs a more precise mathematical formulation. It's unclear how the input data (e.g., channel measurements) are used to estimate the receiver position, and the specific optimization or inference process is not well-defined. Furthermore, the discussion of probabilistic inference with diffusion models is confusing. The paper mentions diffusion models on Page 5 and Page 13, but the connection between these sections is unclear, and the exact training and sampling procedures for the diffusion model are not sufficiently detailed, making it difficult to assess the validity of the approach.

(3) This paper lacks of comparisons with public datasets for channel prediction and other state-of-the-art channel prediction models with NeRF and diffusion models. The absence of comparisons against established benchmarks makes it difficult to gauge the performance of the proposed method relative to existing techniques. Specifically, comparisons with NeRF-based channel prediction methods, which also leverage scene geometry, and other diffusion-based models would be crucial to demonstrate the advantages of the proposed approach.

### Questions
(1) The novelty in the machine learning aspect of this paper is unclear. It appears that the work mainly leverages the equivariant Geometric Algebra Transformer for channel prediction. The authors should clarify which components in the machine learning section present new contributions.

(2) The definitions of inverse problems lack clarity. For instance, the authors should provide a more detailed discussion and formulation for receiver localization. Additionally, the explanations of probabilistic inference with diffusion models on Page 5 are inconsistent with the discussion of diffusion models on Page 13, as the diffusion models used do not seem to follow the standard DDPM framework. The authors should include the training and sampling algorithms for the diffusion model utilized, as well as discuss the model's input.

(3) It would be beneficial to compare the proposed method on public datasets and with other models related to channel prediction, such as NeRF and diffusion models.

(4) Regarding generalization, the authors primarily validate their approach on two different datasets. It would be helpful to consider cross-dataset scenarios to assess performance in unseen conditions. Additionally, the authors should discuss the impact of parameters, such as varying simulated frequencies and the number of paths, on prediction performance.

(5) The authors should proofread the paper to correct typographical errors, such as “The The Tx and Rx locations are sampled uniformly within the bounds of the floor layouts.”

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces Geometric Algebra Transformer (GATr) into wireless channel observation problem and builds a learnable neural simulation surrogate Wi-GATr to predict channel states based on scene primitives. The authors design a Wi-GATr Backbone to exploit the inherent geometric nature of the propagation of wireless signals. Further, they apply this model to probabilistic inference and receiver localization problems. Experimental results show that Wi-GATr outperforms other methods on the two datasets they constructed.

### Strengths
1. They design a new Wireless Geometric Algebra Transformer (Wi-GATr) backbone, which embeds the information of the wireless scene into geometric algebra while the network learns to model the channel.
2. They develop a learnable forward-model for channel simulation and an inverse-model for receiver localization based on the differentiable properties.
3. They build two new datasets with diverse scene geometry.

### Weaknesses
1. The problem of this work is not well identified. The authors only give the formulation of geometric algebra, but do not give any introduction of the wireless channel model. Wireless channels are complex and consist of many parameters. Authors need to specify what information about the channel they want to simulate and predict, such as path loss, shadowing, multipath components, or delay spread. The current description lacks the necessary detail to understand the scope of the simulation.
2. The challenges that need to be addressed are not clearly stated. The authors introduce GATr into this work and build a backbone to make it fit for the wireless channel prediction problem. However, the difficulties and challenges of model transfer are not fully introduced. For example, the adaptation of GATr to handle the specific characteristics of wireless channel data, such as the high dimensionality and sparsity of the channel impulse response, is not discussed. The paper should elaborate on why a standard transformer architecture is insufficient and what specific modifications are necessary.
3. The innovation is somewhat limited. In addition to the designed backbone, the rest of the work consists only of two application experiments using the properties of the existing model. The application to probabilistic inference and receiver localization, while interesting, does not demonstrate a significant methodological advancement beyond the core model. The paper needs to show more novel use cases or a deeper investigation of the model's capabilities.
4. The explanation for some of the pictures is inadequate. For example, Figure 1 shows the geometric surrogates for modeling wireless signal propagation. However, there is not enough explanation of this figure in the paper. It's hard to get the main point of it. The paper should provide a more detailed explanation of how the geometric surrogates relate to the actual physical propagation of wireless signals, including the underlying assumptions and approximations.

### Questions
1. How were the two datasets generated? Were they extracted from other datasets or were they simulated themselves using other tools. Is this sufficient as one of the contributions of the paper?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Wi-GATr, a novel learnable neural surrogate for wireless channel simulation that leverages geometric primitives such as 3D surfaces, antenna positions, and orientations. The primary focus is on addressing limitations in wireless signal propagation modeling by integrating geometric algebra transformers (GATr), which enhance efficiency and accuracy. Wi-GATr is shown to outperform existing models in tasks like signal strength prediction and receiver localization, achieving significant error reductions compared to existing methods.

### Strengths
The paper presents a new approach, Wi-GATr, which is a neural surrogate for wireless channel modeling using Geometric Algebra Transformers, a technique not widely applied in this field. This originality sets it apart from traditional methods by addressing key limitations in differentiability and scalability. The research is supported by thorough empirical evaluations across both simulated and real-world datasets, showing substantial improvements. 
The introduction of two new datasets, Wi3R and WiPTR, further enhances the credibility and reproducibility of the results. The methodology and results are clearly presented. In terms of significance, this work makes contributions to both wireless communication and machine learning.

### Weaknesses
1. Adam is commonly used in deep learning applications, particularly image-processing tasks. However, wireless signal modeling involves different characteristics and challenges than image data. The authors would benefit from a more detailed discussion on why Adam was chosen, especially considering the fundamental differences between wireless signal modeling and typical image tasks.

2. Wi-GATr’s generalization capabilities come from the E(3)-equivariant design of the Geometric Algebra Transformer (GATr). It would be valuable for the authors to provide more justification or discussion regarding their contribution and novelty in implementing or improving such a design.

3. While the authors introduced their own datasets (Wi3R and WiPTR), the authors should provide a clearer justification for their choice of benchmarks, and using more widely recognized simulators such as WinProp or Wireless InSite could strengthen their work.

### Questions
Listed above.

### Soundness
4

### Presentation
3

### Contribution
3

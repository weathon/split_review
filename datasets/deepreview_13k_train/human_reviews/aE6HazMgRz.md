# Spatio-temporal Twins with A Cache for Modeling Long-term System Dynamics

- Decision: Reject
- Scores: 5, 5, 5, 5

## Abstract
This paper investigates the problem of modeling long-term dynamical systems, which are essential for comprehending fluid dynamics and astrophysics. Recently, a variety of spatio-temporal forecasting approaches have been proposed, which usually employ complicated architectures (e.g., Transformer) to learn spatial and temporal relationships. However, these approaches typically perform poorly for long-term forecasting due to information loss during exploration and iterative rollouts. To tackle this, we propose a new framework named Spatio-temporal Twins with A Cache (STAC) for long-term system dynamics modeling. To investigate spatio-temporal relationships from complementary perspectives, STAC contains a frequency-enhanced spatial module and an ODE-enhanced temporal module. Then, we fuse the information between twin modules with channel attention for discriminative feature maps. To capture long-term dynamics, we introduce a cache-based recursive propagator, which stores the previous feature maps in the cache memory during recursive updating. Moreover, we involve both teacher forcing with Mixup and semi-supervised adversarial learning to enhance the optimization process. Extensive experiments show that the proposed STAC can achieve superior performance to existing state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on the long-term spatiotemporal dynamics modeling. They propose the STAC by combing the advanced spatial and temporal modeling backbones and presenting a cache-based recurrent propagator to store the previous feature maps to avoid information loss. Besides, the authors propose a compound training loss to optimize STAC. Experimentally, STAC shows favorable performance in a wide range of benchmarks, including the newly generated flame flow field benchmark.

### Strengths
1.	This paper presents the STAC model to tackle the problem in long-term dynamic prediction, which is technologically reasonable.

2.	The authors experiment on a wide range of benchmarks to demonstrate the effectiveness of STAC.

3.	This paper is clearly presented and well-written.

### Weaknesses
1. About the novelty.

Generally, I think the technology design is reasonable. However, in my opinion, I think it is insufficient in novelty. STAC just combines a series of advanced models, including FNO, Vision Transformer, Neural ODE and a similar recall mechanism proposed by E3D-LSTM. The proposed training strategy is also in a combination style. For me, it is hard to find the novel part in this model.

Note that I am not attempt to enforce the authors to build a completely new model or block. I just think they fail in illustrating their advantages beyond other models. For example, they should consider the following questions:

- Why should they combine vision transformer and FNO? FNet [1] has shown that the feedforward layer can perform like FFT. Why not just only use Transformer or FNO?

- Why can Neural ODE capture the continuous dynamics? I know that Neural ODE can achieves the adaptive depth or adaptive temporal interval. But according to the equation and code, I think the usage here is equivalent to a simple rk4 algorithm. It is hard to claim that they learn the continuous dynamic feature. Besides, They don’t present the necessity in using Neural ODE.

- Are the experimental datasets temporally irregular? According to the paper, I think the input sequences are equally collected along the temporal dimension.

- About the cache-based design. I think it is necessary to demonstrate its advancement over the temporal recall gate in E3D-LSTM.

[1] FNet: Mixing Tokens with Fourier Transforms, ACL 2022.

2. About the experiment.

(1) In addition to the performance, they should compare the efficiency with other baselines, including running time, GPU memory and parameter size.

(2) In the current version, they only compare STAC with video prediction baselines. How about the advanced neural operators, such as LSM [2], U-NO [3]?

(3) Are all the baselines trained by the same loss as STAC? This point is essential to ensure a fair comparison.

(4) More detailed ablations are expected. They should also conduct the following experiments:

- Removing FNO or Transformer in FSM.

- Replacing OTM with ConvLSTM or PredRNN.

- Replacing the CRP with the recall gate in E3D-LSTM.

### Questions
All the questions are listed above, including novelty, experiment design. Here are several serious problems that should be clarified:

(1) The acutal usage of OTM is inconsistent to their expection.

(2) Are all the baselines trained by the same loss?

(3) More neural operator baselines are expected.

(4) Demonstrate the novelty of STAC.

I think it is favorable that the authors experiment on extensive benchmarks. But I have some serious concerns. if the authors reply my questions properly, I am willing to raise my score.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper investigates the problem of modeling long-term dynamical systems, which are essential for understanding fluid dynamics, astrophysics, earth science, etc. The authors propose a new approach called STAC, which contains a discrete frequency-enhanced spatial module and an ODE-enhanced temporal module to capture spatial-temporal relationships of the observational data and employs a cache-based recurrent propagator to ensure the long-term prediction ability of the framework. They also utilize teacher forcing and semi-supervised adversarial learning to stabilize the learning process and enhance the reality of predicted trajectories, respectively. Moreover, the paper constructs a new benchmark (FIRE) to model fire dynamics for dynamics forecasting, which potentially benefits the research community. Extensive experiments on complex dynamics modeling, extreme local events sensing, and video prediction tasks demonstrate the superior performance of the proposed framework compared to other SOTA methods.

### Strengths
1.	This paper tackles an important research problem, complex dynamical system modeling, which benefits our understanding of fluid dynamics, astrophysics, earth science, etc.
2.	This paper provides a well-prepared benchmark, FIRE, to facilitate the research in this field and benefit the community.
3.	This paper proposes to consider spatial-temporal correlations in observational data during prediction by utilizing vision Transformer, Fourier neural operator, and neural ODEs, and incorporating cache memory concept into long-term system modeling.
4.	The authors conduct extensive experiments to verify the performance of the dynamical modeling of the proposed methods from multiple perspectives.

### Weaknesses
1.	The design of the whole framework is complicated. Although the author explains the reason why they design each module, it still lacks straightforward motivation. Do such challenges really exist in the real data? This straightforward utilization of existing techniques makes the paper novelty seem incremental.
2.	The pictures in Figures 3, and 4 do not seem to show a significant improvement of STAC compared to other SOTA methods in terms of visualization.
3.	In the part of the ablation study, some designs, for example, TF/M, CA, and SSAL, only contribute slightly improvement. However, SSAL may make the training of the framework become unstable. Others may increase the time complexity of the framework, which the authors do not report.
4.	Some notations in the paper are confusing. For example, in Section 4.3, the notation definitions of input, feature map, and output are hard to match the subsequent statement.

### Questions
1.	Can authors provide their motivation for such complicated module design through data?
2.	Can authors provide the standard deviation of their experimental results?
3.	The authors can conduct more persuasive experiments to address my concerns mentioned in the Weaknesses part.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the problem of modeling long-term dynamical systems in fields such as fluid dynamics, astrophysics, and earth science. Existing spatio-temporal forecasting approaches based on complex architectures like Transformers have limitations in long-term scenarios due to information loss during semantics exploration and iterative rollouts. To overcome these limitations, the paper proposes a new approach called Spatio-temporal Twins with a Cache (STAC) for long-term system dynamics modeling. STAC comprises a frequency-enhanced spatial module and an ODE-enhanced temporal module that investigates spatio-temporal relationships from complementary perspectives. The information from these twin modules is fused using channel attention to generate informative feature maps. To enhance long-term prediction, a cache-based recurrent propagator is introduced to store and utilize previous feature maps. The paper introduces a new flame flow field benchmark and conducts comprehensive validations across 14 benchmarks. Experimental results demonstrate that STAC outperforms other methods in long-term spatio-temporal prediction and partial differential equation-solving challenges. The contributions of the paper include the construction of a fire dynamics benchmark, the incorporation of cache memory concept into long-term system modeling, the proposal of a novel framework, and extensive experiments showcasing the effectiveness of STAC.

### Strengths
The strengths are as follows:

1. Effective modeling of long-term dynamical systems: The proposed STAC approach overcomes challenges in long-term forecasting by capturing spatio-temporal relationships and leveraging historical information.

2. Integration of cache memory: By incorporating a cache-based recurrent propagator, the model effectively stores and reuses informative feature maps, enhancing the accuracy of long-term predictions.

3. Comprehensive experimental validation: The paper includes extensive experiments on various benchmarks, demonstrating the superior performance of STAC in long-term spatio-temporal prediction and partial differential equation-solving challenges.

4. Information fusion: STAC combines complementary perspectives through twin modules, using channel attention to generate feature maps with rich semantics, leading to more informative predictions.

5. Effective optimization strategies: The paper employs teacher forcing, adversarial learning, and mixup techniques to stabilize the learning process and improve the accuracy of iterative updating.

### Weaknesses
My main concern about this paper is several potential drawbacks:

1. Lack of truly innovative contributions: While the paper introduces several components and techniques, such as FSM, OTM, IFTM, CRP, Fourier-based Spectral Filters, teacher forcing, adversarial learning, and the new FIRE dataset, only CRP and IFTM can be considered as relatively novel contributions. The other techniques mentioned are already known and used in existing methods, which may limit the originality and novelty of the proposed approach.

2. Limited explanation for the CRP technique: The paper mentions the use of a cache-based recurrent propagator (CRP) to prevent forgetting previous events and enhance long sequence prediction. However, it does not provide a clear explanation of the key parameter "$\alpha$" and whether it is a learnable parameter. Additionally, CRP's similarity to traditional RNNs raises questions about its parallelization capabilities and potential limitations.

3. Artificial handling and limited interpretability of IFTM: The separation of temporal and spatial processing, as well as the channel-independent merging in IFTM, appears to be a forced transformation without much interpretability. The lack of learnable factors and reliance on manual processing may hinder the scalability and extensibility of the method.

4. Potential loss of spatial information in FSM: FSM applies different treatments to the same data and forcibly merges them, potentially leading to a loss of spatial information. Additionally, the direct fully connected mapping of the segmented data raises concerns about the preservation of spatial relationships and the possibility of information loss.

### Questions
My questions and concerns about this paper are listed in the Weakness part. I will raise my rating if the author can address my concerns with reasonable evidence.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a framework called Spatio-Temporal Twins with a Cache (STAC) for modeling long-term dynamics of physical systems. The key ideas are: 1) Using a frequency-enhanced spatial module and an ODE-enhanced temporal module to model spatial and temporal relationships from complementary perspectives; 2) Introducing a cache-based recurrent propagator to store historical feature maps; 3) Optimizing the model with techniques like teacher forcing, Mixup, and adversarial learning. The authors construct a new fire dynamics benchmark and evaluate STAC on 14 datasets, showing superior performance over baselines.

### Strengths
1. The problem of modeling long-term dynamics is important with many applications. This paper provides a novel perspective by using a cache memory to enhance long-term dependencies.
2. The motivation is intuitive and reasonable.
3. This paper is well organized and clearly written.
4. The new fire dynamics benchmark (FIRE) constructed in this work could facilitate future research in this domain.
5. Comprehensive experiments on 14 datasets demonstrate the effectiveness and generalizability of the proposed STAC framework.

### Weaknesses
1. Though this paper seems to be promising, I have to say that the novelty seems to be limited. The spatio-temporal twins are actually a two-branch model. Using frequency-based approaches in the spatial domain is nothing new. The temporal module is similar to SimVP v2's [1] but with an ODE solver. The cache memory [2] is also well developed. 
2. I really appreciate the experiments in this paper. However, the ablation study is not satisfying. The authors reported only one metric (RMSE) on only one dataset (Spherical Shallow Water). A more detailed ablation study is needed to figure out why this approach works.
3. It lacks of complexity comparison. The authors should report the parameters and FLOPs of these baseline models.

### Questions
1. Please discuss the differences between STAC and other similar models.
2. Could you add a more detailed ablation study? Considering there are many components, a more detailed ablation study can provide more valuable insights.
3. Please discuss the complexity of these models.

I'm willing to raise my score once these issues have been well solved.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

# Geometric Graph Neural Network based track finding

- Decision: Reject
- Scores: 5, 6, 5

## Abstract
An essential component of event reconstruction in particle physics experiments is identifying the trajectory of charged particles in the detector.   Traditional methods for track finding are often complex, and tailored to specific detectors and input  geometries, limiting their adaptability to new detector designs and optimization processes.
To overcome these limitations, we present a novel, end-to-end track finding algorithm that is detector-agnostic and can take into account multiple input geometric types. To achieve this, our approach unifies  inputs from multiple sub-detectors and detector types into a single geometric algebra representation, simplifying data handling compared to traditional methods.
Then, we leverage an equivariant graph neural network, GATr, to perform track finding across all data from an event simultaneously. 
We validate the effectiveness of our pipeline on various detector concepts with different technologies for the FCC-ee at CERN, specifically the IDEA and CLD  detectors.
This work generalizes track finding across  diverse types of input geometric data and  tracking technologies, facilitating the development of innovative detector concepts, accelerating detector development cycles, and enabling comprehensive detector optimization.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper works on a very unique application of machine learning, related to event trajectory reconstruction for particle physics experiments. Although work has been done on solving this problem in the past with machine learning, this work is detector agnostic. They heavily rely on a previously published graphical learning work, GATr, and modify it to suit their needs.

### Strengths
- The losses L_B, L_V that they introduced are novel and add integrate voltage prediction into the learning pipeline. The experimental results are also very convincing.

### Weaknesses
 - This paper is not ready yet at its current iteration for a machine learning conference. The presentation isn’t very clear and I failed to understand the technically novel aspects of this paper. A decent portion of the paper (e.g. Figs. 1,2 ) doesn’t add anything to my understanding of the technically novel machine learning aspects of this paper.
- A lot of the time they refer the readers to read other papers to understand further important details of their paper. When writing papers, it is indeed very difficult to determine how much do the authors need to explain wrt the past works. However, in this situation, they could have used the space available to write more detailed explanations of their works. Please refer to the StyleGAN paper and some other papers using styleGAN to see how to present past SOTA work and using that to build your own case:
  - Analyzing and Improving the Image Quality of StyleGAN https://openaccess.thecvf.com/content_CVPR_2020/papers/Karras_Analyzing_and_Improving_the_Image_Quality_of_StyleGAN_CVPR_2020_paper.pdf
  - Encoding in Style: a StyleGAN Encoder for Image-to-Image Translation https://openaccess.thecvf.com/content/CVPR2021/papers/Richardson_Encoding_in_Style_A_StyleGAN_Encoder_for_Image-to-Image_Translation_CVPR_2021_paper.pdf

### Questions
- It will help to put this paper under a very granular machine learning category and write it from that perspective. I understand that this work is trying to do temporal graphical structure prediction, but it needs a few more details regarding what category it falls under: multi-modal learning? multi-Domain learning? Multi-stream learning? Data preprocessing and transformation? Cyclic time-series event detection? Etc.
- Please make it way more clear what losses are being used to train which aspects of their Graphical NN. Also, how the representations learned are being used to at run time to reconstruct the trajectories? Fig. 3 is supposed to do that but it is not helping at all.

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
The paper presents the Geometric Graph Track Finding (GGTF) method for particle track finding in collider experiments. GGTF combines data from various sub-detectors using a unified geometric algebra representation. The method employs the Geometric Algebra Transformer to efficiently handle diverse geometric input types, making it adaptable to different detector technologies. GGTF demonstrates high efficiency in reconstructing particle trajectories, particularly excelling with displaced and low-momentum tracks, surpassing traditional techniques.

### Strengths
The paper presents a highly original and impactful method for particle track finding, the Geometric Graph Track Finding (GGTF), which leverages geometric algebra and an equivariant graph neural network (GNN) to overcome limitations in traditional, detector-specific approaches. By unifying data from multiple sub-detectors through geometric algebra, GGTF enables a detector-agnostic solution adaptable to various complex detector configurations, including those proposed for FCC-ee. The thorough experimental validation on different detector concepts demonstrates GGTF’s high quality, showing clear improvements in tracking efficiency and accuracy for challenging cases like low-momentum particles and displaced tracks.

### Weaknesses
I have several concerns as follows:
1. What's the definition of CT! in L356?
2. It would be better if the authors could compare their approach with some other GNN methods.
3. It would improve the paper if the authors provided more detailed descriptions of the experimental data, such as dataset size and model training parameters.
4. Why did the authors choose HDBSCAN, and could they compare it with some other methods?

### Questions
I have listed my questions in weakness section.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes to use  machine learning approach to perform track finding in particle physics.Itdesigned a detector-agnostic model that can beadaptedto differentdetector types.

Ageometric algebra representation in which hitscanbe represented as different geometric objects and transformationsis used to handle input from differentdetectorsandan equivariant graph neural network(GNN)calledGATr, capable of handling multiple geometricinput types from various sub-detectorsis utilized toidentify track pattterns.

The key components are the  following:
1. The unifiedGeometric Algebra Representationsimplifiesintegrating diverse detector data, providingconvenience for subsequent procedures.

2. Equivariant GNN (GATr)utilizes geometric propertiesofdetector data, helping identify patterns regardless ofdetector design. The Object Condensation Lossclusters hits belonging tothe same object close in the embedding space,allowing more efficient reconstruction.

3. The experiments demonstrate the universality of theproposed model and the better track findingresultbroughtby thewell-designed model architecture.

### Strengths
The unified method for track findingcan largely facilitate track finding in particle physicsThe paper is well written, easy to read and self-contained despite building on a larger bodyof particle physics.

The basic idea appearsquiteusefulin particle physics: The ability to performdetector-agnostic track finding brings about applicability across different experimental setups. The unified geometric representation simplifies data handling and reduces complexity compared to traditional methods. The experiments demonstrated high tracking efficiency and accuracy on both the CLD and IDEA detectors, showcasing its versatility and robustness inreal-world applications.

### Weaknesses
1.It seems that the main components of the proposedmodelare borrowed form existing works(i.e. Geometric algebra transformer)and the modules proposed by authors aresomewhatlimited. Is it a combination of existing workfor a particle physics problem?

2.Lackof explanations of model details and technicalroute selection. More extensiveexperiments for ablative study of key components areneededto demonstrate the contributionofeach part.

3.The key aspects are notvery relevant withmachinelearningas anICLR submission. Moreanalysis from the machine learning perspective is needed. I think thesubmitted main contentorrepresentation does fit for a machine learning conference well.

### Questions
Canyou provide some related papersinmachine learning conferencesfocusing on trackfinding in particle physicsorsimilartopics?

Arethere any ablativeexperimentsdemonstratingthe contributionsofthemajor parts tothe final performance?The experiments just shows improved tracking trackingefficiencyunder different definitions andwhichpart takes that increment are notwell-addressed.

L270~L272: output of hits belonging to the same track to be close ina low dimensional embedding space and thosebelonging to different tracks to be faraway.
Have you tried some more advancedcontrastive learning methods toachievethis?

### Soundness
2

### Presentation
3

### Contribution
2

### Summary

This paper introduces a method for predicting the behavior of fluids in novel scenarios based on visual observations. The key innovation is learning a latent representation of the fluid's physical properties from a single 3D video, allowing the model to simulate unseen fluid dynamics without explicit knowledge of its physical parameters. The approach consists of three stages: pretraining, inference, and transfer. In the pretraining stage, the model learns a probabilistic fluid simulator on particle datasets with varying physical parameters. During inference, the model adapts the simulator to new scenes by estimating latent posteriors from visual inputs. Finally, in the transfer stage, the model fine-tunes the physical prior learner using the adapted latent variables to enable novel scene simulations. The authors validate their method on synthetic datasets and demonstrate its ability to generalize to unseen geometries and boundary conditions. They also show that the model can simulate heterogeneous fluids with multiple types of fluid properties.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper presents a novel approach to fluid simulation that leverages visual observations to infer hidden physical properties. This "intuitive physics" method allows for more flexible and generalizable fluid simulations compared to traditional approaches that require explicit knowledge of physical parameters.

- The three-stage training pipeline (pretraining, inference, transfer) is well-structured and theoretically sound. The pretraining stage provides a strong foundation for learning the probabilistic fluid simulator, while the inference stage enables adaptation to new scenes. The transfer stage further refines the model's ability to simulate unseen scenarios.

- The paper provides extensive quantitative and qualitative results demonstrating the effectiveness of the proposed method. The experiments cover various scenarios, including unseen geometries, boundary conditions, and fluid types. The results show that the model can generalize well to novel situations and outperform existing methods in terms of prediction accuracy.

- The paper is well-written and organized, with clear explanations of the methodology and experimental setup. The figures and tables are informative and effectively support the text.

### Weaknesses

#### Some Related Works


#### comment

 - The method relies on a single 3D video as input, which limits its applicability to more complex real-world scenarios. In many practical applications, multiple viewpoints or time-lapse sequences are often available, which could provide richer information for inferring physical properties and improving simulation accuracy. The reliance on a single viewpoint introduces a significant constraint, as real-world fluid dynamics are inherently three-dimensional and depend on multiple spatial dimensions. This limitation is particularly problematic when dealing with complex fluid phenomena such as vortex shedding or turbulent flows, where a single viewpoint may not capture the full extent of the dynamics.

- The paper does not address the issue of noisy or incomplete visual inputs, which are common in real-world scenarios. In practical applications, the visual data may be corrupted by sensor noise, occlusions, or missing frames, which could affect the accuracy of the inferred physical properties and the quality of the simulated results. The absence of any robustness analysis or discussion on how the method would handle such data is a significant weakness. For instance, if the visual input is significantly degraded, the latent posterior estimation could be inaccurate, leading to poor simulation results. The paper should explore methods to mitigate the impact of noisy or incomplete data, such as using robust estimation techniques or incorporating uncertainty modeling into the latent space.

- The evaluation is primarily based on synthetic datasets, which may not fully capture the complexities of real-world fluid dynamics. While synthetic data allows for controlled experiments and quantitative evaluation, it may not accurately represent the challenges and variations encountered in real-world scenarios, such as complex geometries, turbulent flows, or interactions with external forces. The lack of evaluation on real-world data makes it difficult to assess the practical applicability of the method. The paper should include experiments on real-world datasets to demonstrate the method's robustness and generalizability.

- The paper does not provide a detailed analysis of the computational cost and scalability of the proposed method. The authors should discuss the computational complexity of the different stages of the pipeline, including the pretraining, inference, and transfer stages. They should also analyze the memory requirements and runtime performance of the method, especially when dealing with high-resolution simulations or complex fluid dynamics. The lack of information on computational cost makes it difficult to assess the practical feasibility of the method for large-scale simulations. The paper should provide a detailed analysis of the computational resources required for training and inference, as well as the scalability of the method with respect to the size of the simulation domain and the number of particles.

### Suggestions

The paper presents an interesting approach to fluid simulation using visual observations, but there are several areas where the methodology and evaluation could be improved. First, the reliance on a single 3D video input is a significant limitation that needs to be addressed. Future work should explore methods to incorporate multiple viewpoints or time-lapse sequences to provide a more comprehensive understanding of the fluid dynamics. This could involve developing techniques to fuse information from different viewpoints or using a recurrent neural network to process temporal sequences of frames. Furthermore, the paper should investigate the impact of different camera viewpoints on the accuracy of the inferred physical properties and the quality of the simulated results. It would be beneficial to explore how the method performs when the camera is not optimally positioned to capture the fluid dynamics, such as when it is too close or too far from the fluid body, or when it is viewing the fluid from an angle that is not aligned with the primary direction of motion. This would provide a more realistic assessment of the method's robustness and applicability to real-world scenarios.

Second, the paper needs to address the issue of noisy or incomplete visual inputs. The current method does not seem to account for the presence of sensor noise, occlusions, or missing frames, which are common in real-world applications. Future work should explore methods to make the method more robust to such data. This could involve using robust estimation techniques, such as RANSAC, to filter out outliers in the visual data or incorporating uncertainty modeling into the latent space to account for the uncertainty in the inferred physical properties. The paper should also investigate the impact of different levels of noise and incompleteness on the accuracy of the simulated results. It would be beneficial to explore how the method performs when the visual data is significantly degraded, such as when it is corrupted by high levels of noise or when it is missing large portions of the frames. This would provide a more realistic assessment of the method's practical applicability.

Finally, the evaluation of the method should be extended to include real-world datasets. The current evaluation is primarily based on synthetic datasets, which may not accurately represent the complexities of real-world fluid dynamics. Future work should include experiments on real-world datasets to demonstrate the method's robustness and generalizability. This could involve using publicly available datasets of fluid flows, such as those obtained from wind tunnels or laboratory experiments. The paper should also investigate the impact of different real-world factors, such as lighting conditions, camera calibration, and fluid viscosity, on the accuracy of the inferred physical properties and the quality of the simulated results. It would be beneficial to explore how the method performs when the real-world data is significantly different from the synthetic data used in the current evaluation. This would provide a more realistic assessment of the method's practical applicability.

### Questions

- How does the method handle noisy or incomplete visual inputs? What is the impact of sensor noise, occlusions, or missing frames on the accuracy of the inferred physical properties and the quality of the simulated results?

- How does the method perform when the camera viewpoint is not optimally positioned to capture the fluid dynamics? What is the impact of different camera viewpoints on the accuracy of the inferred physical properties and the quality of the simulated results?

- How does the method scale with the size of the simulation domain and the number of particles? What is the computational complexity of the different stages of the pipeline, and how does it affect the runtime performance and memory requirements?

- How does the method perform on real-world datasets? What are the challenges and limitations of applying the method to real-world scenarios, and how can these challenges be addressed?

- What is the impact of different real-world factors, such as lighting conditions, camera calibration, and fluid viscosity, on the accuracy of the inferred physical properties and the quality of the simulated results?

- How does the method compare to other state-of-the-art methods for fluid simulation in terms of accuracy, efficiency, and generalizability?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********

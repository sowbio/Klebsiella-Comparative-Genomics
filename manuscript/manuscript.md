# Comparative Genomic Characterization of Klebsiella pneumoniae ST307 and ST258 Isolates: Antimicrobial Resistance, Pangenome and Core-Genome Phylogeny
## Abstract

## Abstract

Background: 
Klebsiella pneumoniae is a major opportunistic pathogen in which the global dissemination of multidrug-resistant high-risk clones represents an important public health concern. Among these, ST258 has historically contributed to the international spread of KPC carbapenemases, whereas ST307 has emerged as an increasingly important multidrug-resistant lineage. This study compared the genomic characteristics, antimicrobial resistance determinants, virulence-associated loci, pangenome composition, and core-genome relationships of K. pneumoniae ST307 and ST258 isolates.

Methods:
Five K. pneumoniae genomes, comprising four ST307 isolates (KP1766, KP1768, NR5632, and SRR7345603) and one ST258 isolate (NJST258_1), were analyzed using a comparative whole-genome sequencing workflow. Genome assembly and annotation were combined with multilocus sequence typing, AMRFinderPlus-based antimicrobial resistance characterization, Kleborate-based virulence and surface antigen analysis, plasmid replicon detection, Panaroo pangenome analysis, and maximum-likelihood core-genome phylogenetic reconstruction.

Results:
MLST assigned four isolates to ST307 and NJST258_1 to ST258. The ST307 isolates shared the KL102 capsular locus, whereas the ST258 isolate carried KL107. Extensive but heterogeneous antimicrobial resistance profiles were identified. KP1766 and KP1768 carried blaKPC-2, NR5632 carried blaKPC-33, and NJST258_1 carried blaKPC-3, whereas no KPC-type carbapenemase determinant was detected in SRR7345603. blaCTX-M-15 was detected in all ST307 isolates. Major Kleborate virulence loci, including yersiniabactin, colibactin, aerobactin, salmochelin, RmpADC, and rmpA2, were not detected, resulting in a virulence score of 0 for all isolates. An IncFIB(K) replicon was identified in SRR7345603, although no AMRFinderPlus resistance determinant was located on the corresponding contig. Pangenome analysis identified 5,963 gene families, comprising 4,379 core genes (73.4%) and 1,584 shell genes (26.6%). Core-genome genetic distances showed high similarity among ST307 isolates, with KP1766 and KP1768 displaying the smallest pairwise distance (0.000004028), whereas NJST258_1 was substantially more divergent from all four ST307 genomes.

Conclusions:
The analyzed K. pneumoniae ST307 genomes exhibited strong core-genome relatedness but substantial heterogeneity in their antimicrobial resistance determinants, particularly in the distribution of KPC alleles. The ST258 isolate represented a distinct genomic background with a characteristic blaKPC-3-containing resistance profile. These findings illustrate how integration of antimicrobial resistance profiling, pangenomics, and core-genome phylogenetics can resolve genomic diversity among clinically relevant K. pneumoniae high-risk lineages.

### 1. Introduction

Klebsiella pneumoniae is a major opportunistic Gram-negative pathogen responsible for a wide spectrum of infections, including pneumonia, urinary tract infections, bloodstream infections, and other severe healthcare-associated infections. The clinical importance of K. pneumoniae has increased considerably with the global dissemination of multidrug-resistant (MDR) lineages carrying extended-spectrum β-lactamases (ESBLs), carbapenemases, and resistance determinants affecting multiple antimicrobial classes [1,2]. Carbapenem-resistant and third-generation cephalosporin-resistant Enterobacterales are currently classified among the critical-priority bacterial pathogens by the World Health Organization, highlighting the urgent need for improved surveillance and therapeutic strategies [3].

The population structure of K. pneumoniae is highly diverse and comprises numerous clonal lineages differing in antimicrobial resistance, virulence-associated loci, capsular types, and accessory genomic content [1,4]. Whole-genome sequencing (WGS) has therefore become a particularly powerful approach for characterizing clinically relevant K. pneumoniae isolates. Genomic analysis enables simultaneous determination of sequence type (ST), antimicrobial resistance determinants, virulence-associated loci, capsular (K) and O-antigen loci, plasmid-associated sequences, accessory gene content, and phylogenetic relationships [4,5].

Among multidrug-resistant K. pneumoniae, sequence type 258 (ST258) represents one of the best-characterized international high-risk clones. ST258 and the broader clonal group 258 have played a major role in the global dissemination of Klebsiella pneumoniae carbapenemase (KPC)-producing strains [6,7]. Comparative genomic studies have demonstrated that ST258 has a complex evolutionary history involving large-scale recombination and extensive variation in accessory genomic regions, including capsule loci and plasmids [6–8]. The successful association between ST258/CG258 and KPC-encoding mobile genetic elements has contributed substantially to the international spread of carbapenem-resistant K. pneumoniae [6,9].

More recently, ST307 has emerged as another successful international high-risk K. pneumoniae lineage. Genomic epidemiological analyses suggest that ST307 emerged during the mid-1990s and subsequently underwent rapid global dissemination [10]. This lineage has been strongly associated with the ESBL gene blaCTX-M-15 and with additional antimicrobial resistance determinants carried by its accessory genome [10]. Carbapenemase-producing ST307 isolates have subsequently been reported in multiple geographical regions, demonstrating the capacity of this lineage to acquire clinically important carbapenem resistance determinants, including blaKPC genes [11]. In France, genomic surveillance of KPC-producing K. pneumoniae has also identified ST307 among emerging high-risk clones contributing to the dissemination of blaKPC [11].

The success of high-risk K. pneumoniae clones cannot be understood solely through sequence typing. Although isolates belonging to the same ST share a common clonal background, variation in plasmids, mobile genetic elements, antimicrobial resistance genes, surface antigen loci, and other components of the accessory genome can generate substantial genomic and potentially phenotypic diversity [1,12]. Pangenome analysis is therefore particularly informative because it distinguishes the conserved core genome from variable accessory gene content. Combined with core-genome phylogenetic analysis, this approach enables assessment of both evolutionary relatedness and genomic diversification among isolates.

Another important dimension of K. pneumoniae genomic surveillance is the distinction between antimicrobial resistance and hypervirulence. Major acquired virulence loci include the siderophore systems yersiniabactin (ybt), aerobactin (iuc), and salmochelin (iro), the genotoxin colibactin (clb), and the hypermucoidy-associated rmp loci [4,5]. The development of genomic frameworks such as Kleborate has enabled standardized detection of these determinants together with antimicrobial resistance, sequence type, and K- and O-antigen loci [5]. Importantly, antimicrobial resistance and hypervirulence represent distinct but increasingly convergent evolutionary trajectories, making their simultaneous genomic surveillance particularly relevant [4,5].

In this study, we performed a comparative genomic characterization of five K. pneumoniae genomes representing the ST307 and ST258 lineages. We integrated genome assembly and annotation, multilocus sequence typing, antimicrobial resistance determinant detection, virulence and surface antigen characterization, plasmid replicon analysis, pangenome analysis, and core-genome phylogenetic reconstruction. The objectives were to characterize the genomic similarities and differences among the isolates, determine the distribution of antimicrobial resistance and major virulence-associated determinants, evaluate core and accessory genome diversity, and assess the phylogenetic relationships between the ST307 and ST258 genomic backgrounds represented in the dataset.


## 2. Materials and Methods

### 2.1 Bacterial genome dataset
Five Klebsiella pneumoniae genomes were included in the comparative genomic analysis: KP1766, KP1768, NJST258_1, NR5632, and SRR7345603. The SRR7345603 sequencing dataset was retrieved using the Sequence Read Archive (SRA) accession SRR7345603. The genomes were subsequently processed through a comparative genomics workflow including sequence quality assessment, genome assembly and annotation, multilocus sequence typing (MLST), antimicrobial resistance profiling, plasmid analysis, pangenome analysis, core-genome phylogenetic reconstruction, and Kleborate-based genomic characterization.

### 2.2 Quality control of sequencing reads
Raw paired-end sequencing reads from SRR7345603 were assessed using FastQC v0.12.1 prior to downstream processing. The dataset contained 1,597,617 reads for each paired-end file (R1 and R2), corresponding to approximately 237.1 Mbp per file. Read lengths ranged from 35 to 151 bp, with an overall GC content of 56%. No sequences were flagged as poor quality, and the per-base sequence quality module passed for both R1 and R2. Additional FastQC modules were inspected to identify potential sequence-composition biases and other quality issues prior to read trimming.

### 2.3 Read trimming and post-trimming quality control
Paired-end reads were processed using fastp v1.3.6 for quality filtering and read trimming. Prior to filtering, the dataset contained 3,195,234 reads (1,597,617 read pairs), representing 474.24 Mbp. Following processing, 2,708,498 reads (1,354,249 read pairs) passed the filtering criteria, corresponding to approximately 84.8% of the initial reads and 361.81 Mbp of sequence data.

Read filtering substantially improved sequence quality. The proportion of bases with Phred quality scores ≥20 (Q20) increased from 89.14% to 95.17%, while the proportion with scores ≥30 (Q30) increased from 81.68% to 89.57%. Mean read lengths decreased from 148 bp for both R1 and R2 before filtering to 134 bp and 132 bp, respectively, after processing. GC content remained stable, decreasing only slightly from 56.97% to 56.82%. Overall, 2,368 low-quality reads, 1,422 adapter-dimer reads, and 482,946 reads classified as too short were removed during filtering.

Post-trimming read quality was reassessed using FastQC v0.12.1. For both R1 and R2, the per-base sequence quality, per-sequence quality scores, per-base N content, sequence duplication levels, overrepresented sequences, and adapter content modules passed the FastQC quality assessment. A warning remained for the per-sequence GC content and sequence length distribution, while the per-base sequence content module was flagged as failed. The variable sequence-length distribution was consistent with read trimming. Overall, the filtered reads were retained for downstream genome assembly.

### 2.4 Genome assembly
The quality-filtered paired-end reads from SRR7345603 were de novo assembled using SPAdes. The resulting genome assembly was evaluated using QUAST to assess assembly size, contiguity, GC content, and other standard assembly quality metrics. The assembled scaffolds were subsequently used for genome annotation and downstream comparative genomic analyses.

### 2.5 Genome annotation
Genome annotation was performed using Prokka on the SPAdes contig assembly of SRR7345603. The input assembly consisted of 139 contigs and a total sequence length of 5,296,923 bp. Prokka was executed using the genus designation Klebsiella and four CPU threads. The annotation generated standard genomic output files, including GFF, GenBank, nucleotide FASTA, protein FASTA, coding-sequence FASTA, tabular annotation files, and annotation logs. The resulting annotation was subsequently used for downstream comparative genomic analyses.

### 2.6 Multilocus sequence typing (MLST)

Multilocus sequence typing was performed using the mlst software with the Klebsiella-specific MLST scheme. Genome assemblies from the five isolates were screened against the seven housekeeping loci included in the scheme: gapA, infB, mdh, pgi, phoE, rpoB, and tonB. Sequence types were assigned based on the corresponding allelic profiles.

### 2.7 Antimicrobial resistance gene detection

Antimicrobial resistance determinants were identified in the five Klebsiella pneumoniae genome assemblies using AMRFinderPlus. The analysis screened the genome sequences for antimicrobial resistance genes, allelic variants, and resistance-associated point mutations. Detected determinants were classified according to their associated antimicrobial classes, and the resulting AMRFinderPlus outputs were subsequently compared across isolates to characterize differences in their genomic resistance profiles.

### 2.8 Plasmid analysis

Plasmid replicons in the SRR7345603 genome assembly were investigated using PlasmidFinder. Detected replicon sequences were evaluated based on sequence identity, coverage, and their location within the assembled contigs. Contigs carrying plasmid replicons were further examined for plasmid-associated genes and mobile genetic elements. The locations of antimicrobial resistance determinants identified by AMRFinderPlus were also compared with the plasmid-associated contigs to assess potential co-localization of resistance genes.

### 2.9 Pangenome analysis
Pangenome analysis was performed on the five Klebsiella pneumoniae genomes using Panaroo. Genome annotation files were used to construct a gene presence/absence matrix and to classify gene families according to their distribution across the analyzed isolates. Gene families were categorized as core (present in 99–100% of isolates), soft core (95–<99%), shell (15–<95%), or cloud (0–<15%). Panaroo was also used to generate a core-gene alignment for subsequent phylogenetic analysis.

### 2.10 Core-genome phylogenetic analysis

Core-genome phylogenetic relationships among the five Klebsiella pneumoniae isolates were investigated using the filtered core-gene alignment generated by Panaroo. The final alignment comprised 3,953,613 nucleotide positions across the five genomes. Maximum-likelihood phylogenetic inference was performed using IQ-TREE v3.1.3. ModelFinder Plus was used to identify the best-fitting nucleotide substitution model according to the Bayesian information criterion (BIC), resulting in the selection of the TIM+F model. Branch support was evaluated using 1,000 ultrafast bootstrap replicates, and the number of computational threads was automatically determined by IQ-TREE. Maximum-likelihood pairwise genetic distances were additionally obtained from the IQ-TREE analysis to assess the degree of core-genome divergence among isolates.


### 2.11 Virulence, resistance and surface antigen characterization with Kleborate

Virulence-associated determinants and surface antigen loci were characterized using Kleborate. The analysis included screening for the major Klebsiella virulence loci associated with yersiniabactin, colibactin, aerobactin, and salmochelin, as well as the hypermucoidy-associated regulators RmpADC and rmpA2. Kleborate virulence and resistance scores were recorded for comparative analysis among isolates. Capsular (K) and lipopolysaccharide O-antigen loci were also characterized using the Kleborate/Kaptive framework, and the resulting K- and O-locus assignments were compared across the five genomes.

### 2.12 Comparative genomic analysis

Comparative genomic analyses were performed across the five Klebsiella pneumoniae genomes by integrating genome annotation, multilocus sequence typing, antimicrobial resistance, virulence, surface antigen, pangenome, and phylogenetic data. Genome characteristics, including assembly size, number of contigs, predicted coding sequences (CDSs), rRNA genes, tRNA genes, and tmRNA genes, were summarized for each isolate.

Antimicrobial resistance determinants identified by AMRFinderPlus were converted into a binary presence/absence matrix, in which the presence and absence of each detected resistance determinant were encoded as 1 and 0, respectively. This matrix was used to compare resistance profiles among isolates and sequence types.

Kleborate-derived information, including sequence type, major virulence loci, virulence and resistance scores, capsular K loci, and O-antigen loci, was integrated with the genomic dataset. Pangenome gene-content patterns and core-genome phylogenetic relationships were additionally considered to assess genomic similarities and differences among the five isolates.

Because the dataset comprised only five genomes and the objective was comparative genomic characterization, analyses were descriptive and no inferential statistical tests were performed.

## 3. Results

### 3.1 Genome characteristics and annotation

Comparative genome analysis revealed variation in genome size, assembly contiguity, and predicted gene content among the five Klebsiella pneumoniae genomes. Genome sizes ranged from 5,296,923 bp in SRR7345603 to 5,751,187 bp in KP1766. The ST307 genomes KP1766, KP1768, and NR5632 had genome sizes of 5,751,187 bp, 5,745,430 bp, and 5,741,903 bp, respectively, whereas the ST258 isolate NJST258_1 had a genome size of 5,540,936 bp.

The SRR7345603 assembly consisted of 139 contigs totaling 5,296,923 bp. QUAST evaluation of the assembly, using the reported contig-length threshold, yielded a total evaluated length of 5,279,507 bp across 47 contigs, with 36 contigs ≥50 kb. The largest contig was 981,778 bp, the N50 and N90 values were 259,389 bp and 70,128 bp, respectively, and the corresponding L50 and L90 values were 7 and 23. The GC content was 57.46%, and no ambiguous bases were detected (0.00 Ns per 100 kbp).

Genome annotation identified between 4,877 and 5,405 predicted coding sequences (CDSs) across the five genomes. KP1766 contained the highest number of predicted CDSs (5,405), followed by KP1768 and NR5632 (5,398 each), NJST258_1 (5,229), and SRR7345603 (4,877). SRR7345603 additionally contained 19 rRNA genes, 89 tRNA genes, and one tmRNA. The four comparative genomes contained 25 rRNA genes, 77–87 tRNA genes, and one tmRNA each.


### 3.2 Multilocus sequence typing

Multilocus sequence typing separated the five K. pneumoniae genomes into two sequence types. Four isolates, KP1766, KP1768, NR5632, and SRR7345603, were assigned to ST307, whereas NJST258_1 was assigned to ST258.

The ST307 isolates shared the allelic profile gapA(4), infB(1), mdh(2), pgi(52), phoE(1), rpoB(1), and tonB(7). In contrast, NJST258_1 displayed the ST258 allelic profile gapA(3), infB(3), mdh(1), pgi(1), phoE(1), rpoB(1), and tonB(79). Thus, four of the five genomes analyzed belonged to ST307, while a single genome represented ST258.


### 3.3 Antimicrobial resistance profiles

AMRFinderPlus revealed heterogeneous antimicrobial resistance profiles among the five K. pneumoniae genomes. The total number of AMRFinderPlus hits was highest in KP1766 (24), followed by NJST258_1 (23), KP1768 and NR5632 (21 each), and SRR7345603 (13). These hits included acquired resistance genes, allelic variants, and resistance-associated point mutations.

Several resistance determinants were shared by all five isolates. These included blaTEM-1, dfrA14, fosA, the quinolone resistance-associated gyrA_S83I substitution, the parC_S80I substitution, and sul2.

The three ST307 isolates KP1766, KP1768, and NR5632 displayed closely related resistance profiles. All three carried blaCTX-M-15, blaOXA-1, blaSHV-28, blaTEM-1, qnrB1, sul1, sul2, tet(A), catB3, dfrA14, fosA, aac(3)-IIe, aac(6')-33, aac(6')-Ib-cr5, and ant(2'')-Ia. They also shared gyrA_S83I and parC_S80I substitutions and the ompK36_D135DD variant.

Differences were nevertheless observed among these closely related ST307 genomes. KP1766 and KP1768 carried blaKPC-2, whereas NR5632 carried blaKPC-33. KP1766 additionally contained mdrA_D354A and ompK35_Q350Ter, which were not detected in KP1768 or NR5632.

The ST258 isolate NJST258_1 exhibited a distinct resistance profile. It carried blaKPC-3 together with blaOXA-9, blaTEM, blaTEM-1, aac(6')-Ib', aadA1, aph(3'')-Ib, aph(6)-Id, dfrA14, fosA, sul2, oqxA, and oqxB. NJST258_1 also carried both gyrA_S83I and gyrA_D87G, together with parC_S80I, as well as ompK35_E42RfsTer47, phoQ_L96P, and ramR_L111RfsTer13.

SRR7345603 displayed the smallest AMRFinderPlus profile among the five isolates. Its detected determinants included aph(3'')-Ib, aph(6)-Id, blaCTX-M-15, blaSHV-28, blaTEM-1, dfrA14, fosA, qnrB1, sul2, oqxA, and oqxB19, together with the gyrA_S83I and parC_S80I substitutions. Unlike KP1766, KP1768, NR5632, and NJST258_1, no KPC-type carbapenemase determinant was detected in SRR7345603.


### 3.4 Virulence and surface antigen loci

Kleborate analysis did not detect the major virulence loci screened in the five genomes. Yersiniabactin, colibactin, aerobactin, salmochelin, RmpADC, and rmpA2 were absent from all five isolates in the summarized Kleborate results. Accordingly, all isolates received a Kleborate virulence score of 0.

Differences were observed in capsular and O-antigen loci. All four ST307 isolates were assigned to capsular locus KL102, whereas the ST258 isolate NJST258_1 was assigned to KL107. The corresponding K types were reported as unknown (KL102) and unknown (KL107), respectively.

Most isolates carried the OL2α.2 O-antigen locus with predicted O2β type. This profile was observed in KP1768, NJST258_1, NR5632, and SRR7345603. KP1766 differed from the other isolates, carrying OL12 with predicted O12 type.

Kleborate resistance scores also differed among isolates. KP1766 had the highest resistance score (3), followed by KP1768 and NJST258_1 (2 each), while NR5632 and SRR7345603 each had a resistance score of 1.


### 3.5 Plasmid-associated features of SRR7345603

PlasmidFinder identified an IncFIB(K) replicon in the SRR7345603 genome assembly. The detected replicon showed 98.93% nucleotide identity and complete coverage of the reference sequence (560/560 bp). It was located on NODE_33_length_22726_cov_40.357672, a 22,726-bp contig.

Inspection of NODE_33 identified several genes associated with plasmid maintenance, replication, recombination, and mobile genetic elements. These included the RepFIB-associated replication gene repB, sopB, the tyrosine recombinase gene xerD_2, the antirestriction gene klcA_2, umuC_2, and umuD_2. Several insertion-sequence-associated transposases, including IS1222, ISSen4, and IS1A, were also identified on the contig.

None of the antimicrobial resistance determinants identified by AMRFinderPlus in SRR7345603 were located on NODE_33. Thus, the detected IncFIB(K)-associated region was not associated with an AMR determinant in the present assembly-based analysis.


### 3.6 Pangenome structure

Pangenome analysis of the five K. pneumoniae genomes identified a total of 5,963 gene families. Of these, 4,379 were classified as core genes, corresponding to approximately 73.4% of the total pangenome. These gene families were present in 99–100% of the analyzed genomes.

A total of 1,584 gene families, representing approximately 26.6% of the pangenome, were classified as shell genes and therefore constituted the variable component detected among the five genomes. No gene families were assigned to the soft-core or cloud categories under the frequency thresholds applied to this dataset.

These results demonstrate that the majority of gene families were shared across the five genomes, while approximately one-quarter of the identified pangenome represented variable gene content.


### 3.7 Core-genome phylogenetic relationships

The filtered core-gene alignment generated by Panaroo contained 3,953,613 nucleotide positions across the five genomes. Among these positions, 3,933,140 were constant, 20,426 were singleton sites, and 47 were parsimony-informative. Maximum-likelihood phylogenetic analysis was performed using the TIM+F substitution model selected by ModelFinder.

Pairwise maximum-likelihood genetic distances revealed very limited divergence among the ST307 genomes compared with the ST258 isolate. KP1766 and KP1768 displayed the smallest genetic distance in the dataset (0.000004028), indicating very high core-genome similarity. NR5632 was also closely related to these two isolates, with distances of 0.000013663 from KP1766 and 0.000012145 from KP1768.

SRR7345603 showed slightly greater divergence from the other ST307 isolates. Its genetic distances were 0.000021001 from KP1766, 0.000019483 from KP1768, and 0.000029098 from NR5632.

In contrast, NJST258_1 showed substantially greater genetic distances from all four ST307 genomes. Pairwise distances ranged from 0.005175676 between NJST258_1 and SRR7345603 to 0.005192526 between NJST258_1 and NR5632.

The maximum-likelihood tree contained a strongly supported bipartition involving SRR7345603 and NJST258_1 (ultrafast bootstrap support = 100%); however, their comparatively large pairwise genetic distance indicated substantial sequence divergence. Internal relationships among the remaining closely related genomes showed low bootstrap support (31–36%), indicating limited resolution of their precise branching order. Overall, pairwise core-genome distances consistently distinguished the more divergent ST258 isolate NJST258_1 from the closely related ST307 genomes.


### 3.8 Integrated comparative genomic patterns

Integration of MLST, antimicrobial resistance, virulence, surface antigen, pangenome, and core-genome data revealed both shared and isolate-specific genomic features among the five K. pneumoniae genomes. Four isolates belonged to ST307 and shared the KL102 capsular locus, whereas NJST258_1 represented ST258 and carried KL107.

The ST307 genomes KP1766, KP1768, and NR5632 exhibited particularly similar antimicrobial resistance profiles and very small core-genome genetic distances. Nevertheless, differences were observed in carbapenemase alleles, with blaKPC-2 detected in KP1766 and KP1768 and blaKPC-33 detected in NR5632. SRR7345603, although also assigned to ST307 and KL102, displayed a smaller set of AMRFinderPlus hits and lacked a detected KPC carbapenemase determinant.

NJST258_1 differed from the ST307 isolates both by sequence type and core-genome divergence and carried a distinct resistance profile characterized by blaKPC-3 and additional isolate-specific resistance-associated determinants. Despite these differences in resistance profiles, all five genomes lacked the major Kleborate virulence loci examined and had a virulence score of 0.

Together, the comparative analyses identified a large conserved core genome alongside a substantial variable gene component and demonstrated genomic heterogeneity in antimicrobial resistance determinants, surface antigen loci, and core-genome divergence among the analyzed isolates.

## 4. Discussion

The present comparative genomic analysis revealed substantial genomic conservation together with marked heterogeneity in antimicrobial resistance determinants among the five Klebsiella pneumoniae isolates. Four isolates were assigned to the globally disseminated sequence type ST307, whereas NJST258_1 belonged to ST258. Despite the limited number of genomes included in the analysis, integration of MLST, antimicrobial resistance profiling, virulence-associated loci, capsular and O-antigen typing, plasmid replicon detection, pangenome analysis, and core-genome phylogeny highlighted distinct genomic characteristics between and within these two clinically important lineages.

### 4.1 Predominance and genomic similarity of ST307 isolates

Four of the five genomes analyzed belonged to ST307, including KP1766, KP1768, NR5632, and SRR7345603. ST307 has emerged as an internationally disseminated K. pneumoniae lineage frequently associated with multidrug resistance, healthcare-associated infections, and the acquisition of extended-spectrum β-lactamases and carbapenemases [REF]. Its increasing detection across geographically diverse settings has led to its recognition as an important high-risk clone [REF].

The close relationship among the ST307 genomes was supported by their shared MLST allelic profile and their relatively small core-genome genetic distances. KP1766 and KP1768 displayed the smallest pairwise distance (0.000004028), while NR5632 was also closely related to these two isolates. SRR7345603 showed slightly greater divergence from the other ST307 genomes but remained considerably closer to them than to the ST258 isolate.

These findings indicate substantial conservation of the core genome within the ST307 group. However, the differences observed in antimicrobial resistance determinants demonstrate that closely related isolates can nevertheless differ considerably in their accessory resistance content. Such variation is compatible with the dynamic acquisition, loss, or modification of mobile genetic elements and resistance-associated loci within successful K. pneumoniae lineages [REF].

### 4.2 Distinct antimicrobial resistance profiles within ST307

Antimicrobial resistance represented one of the major sources of genomic heterogeneity among the analyzed isolates. KP1766, KP1768, and NR5632 exhibited particularly extensive and similar resistance profiles, including blaCTX-M-15, blaOXA-1, blaSHV-28, blaTEM-1, qnrB1, sul1, sul2, tet(A), catB3, and multiple aminoglycoside resistance determinants.

The presence of blaCTX-M-15 in the ST307 isolates is particularly relevant because ST307 has frequently been associated with CTX-M-15-producing K. pneumoniae [REF]. The combination of an internationally successful clonal background and horizontally acquired resistance determinants may contribute to the persistence and dissemination of this lineage in healthcare environments [REF].

Important differences were nevertheless observed in carbapenemase determinants. KP1766 and KP1768 carried blaKPC-2, whereas NR5632 carried blaKPC-33. In contrast, no KPC-type carbapenemase determinant was detected in SRR7345603. These observations demonstrate that membership of the same sequence type does not imply an identical resistance genotype.

The detection of different blaKPC alleles within closely related ST307 genomes further illustrates the evolutionary plasticity of antimicrobial resistance within this lineage. KPC enzymes represent clinically important class A carbapenemases associated with reduced susceptibility or resistance to carbapenems and other β-lactams [REF]. The distinction between blaKPC-2 and blaKPC-33 may also be clinically relevant because individual KPC variants can differ in their hydrolytic properties and susceptibility to β-lactam/β-lactamase inhibitor combinations [REF].

SRR7345603 differed substantially from the other ST307 isolates by displaying only 13 AMRFinderPlus hits compared with 21–24 in the other extensively resistant ST307 genomes. Nevertheless, it retained several clinically relevant resistance determinants, including blaCTX-M-15, blaSHV-28, blaTEM-1, qnrB1, sul2, dfrA14, aph(3'')-Ib, and aph(6)-Id. Therefore, its comparatively smaller resistance repertoire should not be interpreted as an absence of multidrug-resistance-associated genetic determinants.

### 4.3 Fluoroquinolone resistance-associated determinants

All five isolates carried the GyrA S83I and ParC S80I substitutions. These proteins are components of DNA gyrase and topoisomerase IV, respectively, which are major targets of fluoroquinolone antibiotics. Mutations within the quinolone resistance-determining regions of gyrA and parC are well-established mechanisms contributing to fluoroquinolone resistance in Enterobacterales [REF].

NJST258_1 additionally carried the GyrA D87G substitution, distinguishing it from the ST307 isolates. Plasmid-mediated quinolone resistance determinants were also detected, including qnrB1 in several ST307 isolates. The coexistence of target-site mutations and plasmid-mediated quinolone resistance determinants may contribute to elevated fluoroquinolone resistance levels and facilitate the selection of additional chromosomal mutations under antimicrobial pressure [REF].

Variation in efflux-associated determinants was also observed. SRR7345603 carried oqxA and oqxB19, whereas NJST258_1 carried oqxA and oqxB. These findings illustrate the multiplicity of genetic mechanisms potentially contributing to the quinolone and broader multidrug resistance phenotype of the analyzed genomes.

### 4.4 Distinct genomic characteristics of the ST258 isolate

NJST258_1 was the only ST258 isolate included in the dataset and exhibited a genomic profile clearly distinct from the ST307 isolates. ST258 is a globally recognized high-risk K. pneumoniae lineage historically associated with the international dissemination of KPC carbapenemases [REF].

Consistent with this association, NJST258_1 carried blaKPC-3. It also contained blaOXA-9, blaTEM, blaTEM-1 and several aminoglycoside resistance determinants, including aac(6')-Ib', aadA1, aph(3'')-Ib, and aph(6)-Id. Additional resistance-associated variants included gyrA_D87G, ompK35_E42RfsTer47, phoQ_L96P, and ramR_L111RfsTer13.

Core-genome genetic distances strongly distinguished NJST258_1 from the four ST307 genomes. Distances between NJST258_1 and the ST307 isolates were approximately 0.00518, compared with distances on the order of 10^-5 among the ST307 isolates. This marked difference was consistent with the assignment of NJST258_1 to a separate sequence type and confirms substantial core-genome divergence between the ST258 and ST307 backgrounds represented in this dataset.

### 4.5 Resistance and classical hypervirulence determinants were uncoupled

Despite the extensive antimicrobial resistance repertoires detected in several isolates, none of the five genomes carried the major virulence loci screened by Kleborate. Yersiniabactin, colibactin, aerobactin, salmochelin, RmpADC, and rmpA2 were absent from the summarized profiles, resulting in a virulence score of 0 for all isolates.

This finding is important because antimicrobial resistance and hypervirulence represent distinct genomic characteristics in K. pneumoniae. Classical multidrug-resistant hospital-associated lineages and hypervirulent lineages historically represented partially distinct populations, although convergence between antimicrobial resistance and hypervirulence is increasingly recognized [REF].

In the present dataset, no such convergence was detected based on the major Kleborate virulence markers investigated. In particular, the absence of aerobactin and the rmp-associated loci does not support classification of these genomes as classical hypervirulent K. pneumoniae on the basis of the genomic markers examined.

However, a virulence score of 0 should not be interpreted as evidence that an isolate is biologically avirulent. K. pneumoniae pathogenicity is multifactorial and also depends on factors such as capsule production, lipopolysaccharide, fimbriae, iron acquisition systems not represented by the major hypervirulence score, metabolic adaptation, host susceptibility, and infection site [REF]. The present analysis therefore specifically indicates the absence of the major hypervirulence-associated loci screened rather than an absence of pathogenic potential.

### 4.6 Capsular and O-antigen diversity

Capsular locus analysis showed a strong association with sequence type in this small dataset. All four ST307 genomes carried KL102, whereas the ST258 isolate NJST258_1 carried KL107. This conservation of KL102 among the ST307 genomes provides an additional genomic feature shared by the members of this lineage.

The O-antigen locus showed a different pattern. KP1768, NR5632, SRR7345603, and NJST258_1 carried OL2α.2 with predicted O2β type, despite belonging to two different sequence types. In contrast, KP1766 carried OL12/O12.

The presence of a distinct O locus in KP1766 despite its close core-genome relationship with KP1768 and NR5632 illustrates that surface antigen loci can vary even among genetically closely related isolates. Such variability may arise through recombination and horizontal exchange affecting surface polysaccharide biosynthesis regions [REF].

The distribution of K and O loci is epidemiologically relevant because capsular and O-antigen structures contribute to interactions with the host immune system and are increasingly considered potential targets for vaccines, monoclonal antibodies, and other anti-Klebsiella strategies [REF].

### 4.7 IncFIB(K)-associated region in SRR7345603

PlasmidFinder detected an IncFIB(K) replicon in SRR7345603 with 98.93% identity and complete coverage of the 560-bp reference sequence. The replicon was located on NODE_33, which also contained the plasmid-associated replication gene repB, sopB, xerD_2, klcA_2, umuC_2, umuD_2, and several insertion-sequence-associated transposases.

The combination of the IncFIB(K) replicon and plasmid-associated genes supports the presence of a plasmid-associated region on this contig. IncF-type plasmids are frequently encountered in Enterobacterales and can contribute to bacterial genome plasticity and the dissemination of accessory genes [REF].

Interestingly, none of the AMRFinderPlus resistance determinants detected in SRR7345603 were located on NODE_33. Therefore, the IncFIB(K)-associated region identified in this assembly could not be directly linked to the antimicrobial resistance determinants detected in the isolate.

This result should nevertheless be interpreted cautiously because short-read assemblies frequently fragment plasmids and may not allow complete reconstruction of plasmid architecture. Consequently, the detection of an IncFIB(K) replicon on NODE_33 demonstrates the presence of an IncFIB(K)-associated sequence but does not establish that NODE_33 represents a complete circular plasmid or exclude the localization of resistance determinants on other plasmid fragments.

### 4.8 Pangenome structure reveals a conserved core and variable accessory component

Pangenome analysis identified 5,963 gene families across the five genomes, of which 4,379 (73.4%) were classified as core genes and 1,584 (26.6%) as shell genes. Thus, approximately three-quarters of the detected gene families were conserved across the dataset, while more than one-quarter represented variable gene content.

The predominance of core genes is consistent with the inclusion of genomes belonging to the same bacterial species and, particularly, with four of the five isolates belonging to the same ST307 lineage. Nevertheless, the presence of 1,584 shell gene families demonstrates substantial accessory genomic diversity.

Accessory genome variation is an important component of K. pneumoniae evolution because horizontally acquired regions can encode antimicrobial resistance, mobile genetic elements, metabolic functions, and other traits influencing ecological adaptation [REF]. The differences in AMR determinants observed among the closely related ST307 isolates provide a clear example of how accessory genomic variation can occur despite strong conservation of the core genome.

No soft-core or cloud gene families were identified under the frequency thresholds used. This distribution is strongly influenced by the small number of genomes included in the analysis. With only five genomes, the possible frequency classes are discrete, and some conventional pangenome categories cannot be populated in the same manner as in datasets containing tens or hundreds of genomes. Consequently, the absence of soft-core and cloud genes should not be interpreted as a general biological characteristic of the K. pneumoniae pangenome.

### 4.9 Core-genome phylogeny and genetic distances

Core-genome phylogenetic analysis was based on a 3,953,613-position alignment. The analysis identified 47 parsimony-informative positions and 20,426 singleton sites, indicating relatively limited phylogenetic information for resolving some of the shortest internal branches among the closely related genomes.

Pairwise maximum-likelihood distances provided a particularly informative representation of genomic relatedness. KP1766 and KP1768 were the most similar genomes, with a distance of 0.000004028. NR5632 was also highly similar to both isolates. SRR7345603 was somewhat more divergent within ST307 but remained much closer to the other ST307 isolates than to NJST258_1.

In contrast, NJST258_1 displayed pairwise distances of approximately 0.00518 from each ST307 genome, confirming substantially greater core-genome divergence.

Some internal branches of the maximum-likelihood phylogeny received low ultrafast bootstrap support (31–36%), indicating that the exact branching order among the closely related genomes was not robustly resolved. Although one bipartition involving SRR7345603 and NJST258_1 received 100% bootstrap support, the large genetic distance between these isolates and the overall distance matrix demonstrate that this topology should not be interpreted as evidence that they constitute the most genetically similar pair.

The combination of MLST assignments and pairwise core-genome distances therefore provides a clearer representation of the relationships in this small dataset: KP1766, KP1768, NR5632, and SRR7345603 constitute closely related ST307 genomes, whereas NJST258_1 represents a substantially divergent ST258 genomic background.

### 4.10 Study limitations

Several limitations should be considered when interpreting these findings. First, only five genomes were analyzed, including four ST307 isolates and a single ST258 isolate. The dataset therefore cannot be considered representative of the broader genomic diversity of either lineage, and statistical comparisons between sequence types were not appropriate.

Second, the genome assemblies differed substantially in contiguity. KP1766, KP1768, and NR5632 consisted of three contigs and NJST258_1 of six contigs, whereas SRR7345603 consisted of 139 contigs. Differences in assembly completeness and fragmentation may influence gene detection, plasmid reconstruction, and comparisons of accessory genomic content.

Third, antimicrobial resistance was inferred from genomic determinants rather than experimentally confirmed antimicrobial susceptibility phenotypes in the present analysis. Genotype-based predictions should therefore not be considered equivalent to phenotypic susceptibility testing.

Similarly, virulence was evaluated using genomic markers rather than experimental infection models or phenotypic virulence assays. The absence of the major hypervirulence-associated loci therefore does not demonstrate absence of pathogenic potential.

Finally, plasmid analysis was based on a short-read assembly. Although an IncFIB(K) replicon and several plasmid-associated genes were detected in SRR7345603, complete plasmid reconstruction would require additional evidence, ideally including long-read sequencing or hybrid assembly.

Despite these limitations, the integrated genomic approach used here allowed simultaneous comparison of clonal background, resistance determinants, virulence-associated loci, surface antigens, accessory gene content, plasmid-associated sequences, and core-genome relatedness.


## 5. Conclusion

This comparative genomic analysis revealed substantial core-genome conservation together with considerable antimicrobial resistance and accessory-genome heterogeneity among five Klebsiella pneumoniae isolates. Four isolates belonged to ST307 and shared the KL102 capsular locus, whereas NJST258_1 belonged to the genetically divergent ST258 lineage and carried KL107.

The ST307 genomes were closely related at the core-genome level but differed in their antimicrobial resistance repertoires. Notably, KP1766 and KP1768 carried blaKPC-2, NR5632 carried blaKPC-33, and no KPC determinant was detected in SRR7345603. The ST258 isolate NJST258_1 carried blaKPC-3 and exhibited a distinct resistance-associated genomic profile. These findings emphasize that substantial resistance diversity can occur even among isolates sharing the same sequence type.

None of the five isolates carried the major hypervirulence-associated loci evaluated by Kleborate, and all received a virulence score of 0. Pangenome analysis identified 5,963 gene families, including 4,379 core and 1,584 shell gene families, demonstrating a highly conserved core genome accompanied by a substantial variable genomic component.

An IncFIB(K)-associated region was additionally identified in SRR7345603, although no AMR determinant detected in this isolate was located on the corresponding contig. Overall, the study illustrates the value of integrating genome typing, antimicrobial resistance analysis, virulence profiling, surface antigen characterization, pangenomics, and phylogenetics to resolve genomic similarities and differences among clinically relevant K. pneumoniae lineages.

## References

1. Wyres KL, Lam MMC, Holt KE. Population genomics of Klebsiella pneumoniae. Nat Rev Microbiol. 2020;18(6):344–359. doi:10.1038/s41579-019-0315-1.

2. Holt KE, Wertheim H, Zadoks RN, Baker S, Whitehouse CA, Dance D, et al. Genomic analysis of diversity, population structure, virulence, and antimicrobial resistance in Klebsiella pneumoniae, an urgent threat to public health. Proc Natl Acad Sci U S A. 2015;112(27):E3574–E3581. doi:10.1073/pnas.1501049112.

3. World Health Organization. WHO bacterial priority pathogens list, 2024: bacterial pathogens of public health importance to guide research, development and strategies to prevent and control antimicrobial resistance. Geneva: World Health Organization; 2024.

4. Martin RM, Bachman MA. Colonization, infection, and the accessory genome of Klebsiella pneumoniae. Front Cell Infect Microbiol. 2018;8:4. doi:10.3389/fcimb.2018.00004.

5. Lam MMC, Wick RR, Watts SC, Cerdeira LT, Wyres KL, Holt KE. A genomic surveillance framework and genotyping tool for Klebsiella pneumoniae and its related species complex. Nat Commun. 2021;12(1):4188. doi:10.1038/s41467-021-24448-3.

6. Wyres KL, Hawkey J, Hetland MAK, Fostervold A, Wick RR, Judd LM, et al. Emergence and rapid global dissemination of CTX-M-15-associated Klebsiella pneumoniae strain ST307. J Antimicrob Chemother. 2019;74(3):577–581. doi:10.1093/jac/dky492.

7. DeLeo FR, Chen L, Porcella SF, Martens CA, Kobayashi SD, Porter AR, et al. Molecular dissection of the evolution of carbapenem-resistant multilocus sequence type 258 Klebsiella pneumoniae. Proc Natl Acad Sci U S A. 2014;111(13):4988–4993. doi:10.1073/pnas.1321364111.

8. Bowers JR, Kitchel B, Driebe EM, MacCannell DR, Roe C, Lemmer D, et al. Genomic analysis of the emergence and rapid global dissemination of the clonal group 258 Klebsiella pneumoniae pandemic. PLoS One. 2015;10(7):e0133727. doi:10.1371/journal.pone.0133727.

9. Chen L, Mathema B, Pitout JDD, DeLeo FR, Kreiswirth BN. Epidemic Klebsiella pneumoniae ST258 is a hybrid strain. mBio. 2014;5(3):e01355-14. doi:10.1128/mBio.01355-14.

10. Peirano G, Bradford PA, Kazmierczak KM, Chen L, Kreiswirth BN, Pitout JDD. Importance of clonal complex 258 and IncFK2-like plasmids among a global collection of Klebsiella pneumoniae with blaKPC. Antimicrob Agents Chemother. 2017;61(4):e02610-16. doi:10.1128/AAC.02610-16.

11. Bonnin RA, Jousset AB, Chiarelli A, Emeraud C, Glaser P, Naas T, et al. Emergence of new non-clonal group 258 high-risk clones among Klebsiella pneumoniae carbapenemase-producing K. pneumoniae isolates, France. Emerg Infect Dis. 2020;26(6):1212–1220. doi:10.3201/eid2606.191517.

12. Wyres KL, Wick RR, Gorrie C, Jenney A, Follador R, Thomson NR, Holt KE. Identification of Klebsiella capsule synthesis loci from whole genome data. Microb Genom. 2016;2(12):e000102. doi:10.1099/mgen.0.000102.

13. Feldgarden M, Brover V, Gonzalez-Escalona N, Frye JG, Haendiges J, Haft DH, et al. AMRFinderPlus and the Reference Gene Catalog facilitate examination of the genomic links among antimicrobial resistance, stress response, and virulence. Sci Rep. 2021;11:12728. doi:10.1038/s41598-021-91456-0.

14. Tonkin-Hill G, MacAlasdair N, Ruis C, Weimann A, Horesh G, Lees JA, et al. Producing polished prokaryotic pangenomes with the Panaroo pipeline. Genome Biol. 2020;21:180. doi:10.1186/s13059-020-02090-4.

15. Wong TKF, Ly-Trong N, Ren H, Demotte P, Baños H, Roger AJ, et al. IQ-TREE 3: phylogenomic inference software using complex evolutionary models. Mol Biol Evol. 2026;43(5):msag117. doi:10.1093/molbev/msag117.
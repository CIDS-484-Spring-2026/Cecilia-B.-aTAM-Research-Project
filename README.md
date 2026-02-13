# Research Outline and readMe
## About

This is a Github repository for a research project working on Abstract Tile Assembly Models (aTAM), in which I hope to demonstrate novel results in the computing power of a class of rhombic tiles.

## Background

Abstract Tile Assembly Models (aTAM) is a sub field in self assembly research. *Self assembly* is the process of a collection of simple components autonomously combining into a more complex structure. aTAM is interested in using tile shapes and arranging them via gluing matching sides together. 

![Diagram of an aTAM tile](http://self-assembly.net/wiki/images/9/93/Example-tile.jpg)

In this example, a square tile has two glues, *a* and *b*. Glue *a* has a strength of 2, represented by two squares, and glue *b* has a strength of one. Only a tile with matching glues can connect to this first tile. A square tile with glue *b* on its left side could connect, for example. 

![Diagram of multiple aTAM tiles](http://self-assembly.net/wiki/images/0/05/Counter-border-tiles.png)

Critically: this connection is random. If there are multiple valid connections that could be made, it is not certain which will be made first. 

If you stipulate that tiles can only bind with a combined strength of at least 2, a system of this type is referred to as *temperature* 2, then square tiles are capable of doing universal computation. That is to say, they can assemble themselves in such a way to simulate the behaviors of a computer. 

However, square tiles in temperature 1 systems are not capable of this. Dr. Hendricks, in a previous project, determined that a temperature 1 aTAM system made of *rhombic* tiles was in fact capable of computation. Here is an example diagram of the complicated structure needed for these tiles to read a binary digit.
![Diagram of a bit reader in a rhombic aTAM system.](https://raw.githubusercontent.com/CIDS-484-Spring-2026/sensitivity-analysis-TAM/c5e569bc6524a01262a93663a2c60091764ba740/poster/macro-106_path_g2.svg?token=BFMRRCVDK2OIUUCQAZJGROTJR6JCO)

This construction, however, does not work for all kinds of rhombuses. 
## Goals

My objective is to analyze the special class of rhombuses that elude the construction previously found by Dr. Hendricks. These are the rhombuses found by this equation: β = 180n/(2n − 1) for n ∈ ℕ. An example would be n=2, which would give 120 degrees for the major angle of the rhombus. 

![Diagram of a 120 degree rhombus](example_rhombus.png)

Are these tiles as limited as square tiles in temperature 1 systems? Are they capable of computation via a new construction? Or something in between?

## References

The main reference material that will be used for this project comes from this wonderful resource: the [self-assembly wiki](http://self-assembly.net/wiki/index.php/Main_Page). Not only does this wiki contain articles explaining various concepts in self assembly, it also houses many relevant papers on the subject from which I will conduct my research.

Another important set of references are from the original paper by Dr. Hendricks and Adam Stadick, which can be found in [this Github repository](https://github.com/CIDS-484-Spring-2026/sensitivity-analysis-TAM). This is now available to students taking CIDS 484 this semester.

A fun demonstration of square aTAM systems can be found on this website: [WebTAS](http://self-assembly.net/software/WebTAS/WebTAS-latest/)

## Initial Resources

Selected from the wiki above, of key importance is the paper proving the lack of computability of temperature 1 square tiles. This is [*Limitations of Self-Assembly at Temperature 1*](https://pdf.sciencedirectassets.com/271538/1-s2.0-S0304397510X00275/1-s2.0-S0304397510004585/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC0aCXVzLWVhc3QtMSJIMEYCIQCwSsdW%2FP5KhMFJ7pcJ9TGX3Ikiqc4nHIq35tL%2BWFB%2FqQIhAMUIMFPVfWmghipq6DzJQ0xGHDeWAAi3lFZqyXk7tFAkKrsFCPX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQBRoMMDU5MDAzNTQ2ODY1IgwTbaIH1VmWGoKas6AqjwU2OdgN3rfQTil26L5ccB37IpoVNXRnGPXtQ5dDntp6iyKHfl%2BG6hWk9uSi1KI1ui6F7dEUTkd9CIkhmKgA0BwVRTKP2Fnq1hml3LTXSrcVjPwx%2FTQkC2plfuNJ2gkPMMXezWBZFEXjDZvg7%2B8otiA5rEQAoIWVwdux3m0v8pcShAQ172U2SJ349TgccVl2znW8Ube6cSiEIrsCMuTS%2BowqaRTeFHnSkO4DCEbG2Fev4nWr5YbQkFB7s3Q9k6c2DorLctANAeDOIr88UJOX4wz2edMJKvkwxoCmNKISD53rfixtZRlNUm9u4M1Uml3PjuDxfw%2BaRa55ggK0VfSXrySe1n5mzJiNJeRgvUODDKRtVYXjb3fV3COodmpRRwwEpd1IuLsIF93I%2BuzzBfa35rN4I6f0HHg3H%2FiBv%2FIQh10SMxT%2Fl281m0cIlLjImGpxeaLXVP8%2BXxDMGb7uoEV6D2h4L4VuINEJpS%2B1ZijfFhRbJJldeQu1AlIKL9z2b112Gw%2FVEcweC%2F6D3U4ay7Tm5%2B2ndvnWnm7AVFEUzt9tmkiN0KZKEqZ48%2Brk5%2FoZXjZTa4uwKNJFDQ0gcBGfdf0rBXLdr2RBGhey%2F1twDHDpcMWgsmY0GWAoGo0QVcAr6gU47XagHU11Nh9j5Fd7bxssjl4hH20oL2MpWzCWDHmY2oN%2Byliu53VrANhHS%2FeRVFPQdxGm%2BYRiAjvFts1jm5cinPAxzzLelfGv8%2FjmmqYU6yOTr1QzExzdVAOqyYfUYR5O5FO8oU96rqlqHmtUIKT03oERuhYe%2BGyE7G6x2Zo9OF4%2FFEE1ZG2H6lBKGgiTVtPFJteiL6hH0W8LBWoW7%2Bhvje6Ka6ErjUddRqHUDcJzlKm2MMmOvswGOrABlC%2FRsOOdQy%2Fb2%2FkL94vOJnwHS9Cl%2FACxQG%2Bj40rIWkAignnDnlGgJu2w87WfDyY8W27tKYWAvPKGGw%2FTDV3Zju7vIoyeno0OY%2FZl0nnog2ILAmH9GzGSobaW8N33J29rXsqf9m%2BZYPnOEdvBo0BdD3e%2FwULPe%2BuguVWRg0dWkwjIL2B97xpMqKRrBHD1QRfdfqoKfo9WuDAQDau%2BYb7BAgcnG5vJ5sp8FSCA8vmD6vk%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20260213T205708Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYXL3A5MR7%2F20260213%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=6165d4d29c97af4cecbba759925efc27d2ba0f26a2e72b50be4822d86e054dc9&hash=ad9cd6c912480adf9fac2a9a2ddad82e3b2fc7db20c093b79e9a14ce2ba34026&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S0304397510004585&tid=spdf-0517bf40-0d41-4109-8842-c95da9f746eb&sid=a9a886ff9532114f4308f3096b2bf8616ef8gxrqa&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&rh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=11125a06065655055b&rr=9cd73c84dbfe8710&cc=us) by Doty et. al. 


## ⚠️ Legal & Ethical Disclaimer
#This project is provided as-is, with no guarantees or responsibility from the creator.
# This repository exists strictly for educational, testing, and cybersecurity research purposes.
# The user assumes full legal responsibility for any actions performed with the information provided.
# The developer (pxrb) is NOT responsible for misuse, damage, legal issues, or unethical actions performed by others.
#> If you break the law or violate ethics using this tool, it is 100% your responsibility — not mine.

# MADE BY PXRB - EVADEFBI | Twitter: @evadefbi | Discord: @evadefbi | 
# MIT License on github

import colorama
from colorama import Fore, Style
from colorama.ansi import clear_screen
import dns.resolver
import requests
import socket
import os
import re

gradient_colors = [
(255, 255, 255),
(254, 254, 255),
(253, 253, 255),
(252, 252, 255),
(251, 251, 255),
(250, 250, 255),
(249, 249, 255),
(248, 248, 255),
(247, 247, 255),
(246, 246, 255),
(245, 245, 255),
(244, 244, 255),
(243, 243, 255),
(242, 242, 255),
(241, 241, 255),
(240, 240, 255),
(239, 239, 255),
(238, 238, 255),
(237, 237, 255),
(236, 236, 255),
(235, 235, 255),
(234, 234, 255),
(233, 233, 255),
(232, 232, 255),
(231, 231, 255),
(230, 230, 255),
(229, 229, 255),
(228, 228, 255),
(227, 227, 255),
(226, 226, 255),
(225, 225, 255),
(224, 224, 255),
(223, 223, 255),
(222, 222, 255),
(221, 221, 255),
(220, 220, 255),
(219, 219, 255),
(218, 218, 255),
(217, 217, 255),
(216, 216, 255),
(215, 215, 255),
(214, 214, 255),
(213, 213, 255),
(212, 212, 255),
(211, 211, 255),
(210, 210, 255),
(209, 209, 255),
(208, 208, 255),
(207, 207, 255),
(206, 206, 255),
(205, 205, 255),
(204, 204, 255),
(203, 203, 255),
(202, 202, 255),
(201, 201, 255),
(200, 200, 255),
(199, 199, 255),
(198, 198, 255),
(197, 197, 255),
(196, 196, 255),
(195, 195, 255),
(194, 194, 255),
(193, 193, 255),
(192, 192, 255),
(191, 191, 255),
(190, 190, 255),
(189, 189, 255),
(188, 188, 255),
(187, 187, 255),
(186, 186, 255),
(185, 185, 255),
(184, 184, 255),
(183, 183, 255),
(182, 182, 255),
(181, 181, 255),
(180, 180, 255),
(179, 179, 255),
(178, 178, 255),
(177, 177, 255),
(176, 176, 255),
(175, 175, 255),
(174, 174, 255),
(173, 173, 255),
(172, 172, 255),
(171, 171, 255),
(170, 170, 255),
(169, 169, 255),
(168, 168, 255),
(167, 167, 255),
(166, 166, 255),
(165, 165, 255),
(164, 164, 255),
(163, 163, 255),
(162, 162, 255),
(161, 161, 255),
(160, 160, 255),
(159, 159, 255),
(158, 158, 255),
(157, 157, 255),
(156, 156, 255),
(155, 155, 255),
(154, 154, 255),
(153, 153, 255),
(152, 152, 255),
(151, 151, 255),
(150, 150, 255),
(149, 149, 255),
(148, 148, 255),
(147, 147, 255),
(146, 146, 255),
(145, 145, 255),
(144, 144, 255),
(143, 143, 255),
(142, 142, 255),
(141, 141, 255),
(140, 140, 255),
(139, 139, 255),
(138, 138, 255),
(137, 137, 255),
(136, 136, 255),
(135, 135, 255),
(134, 134, 255),
(133, 133, 255),
(132, 132, 255),
(131, 131, 255),
(130, 130, 255),
(129, 129, 255),
(128, 128, 255),
(127, 127, 255),
(126, 126, 255),
(125, 125, 255),
(124, 124, 255),
(123, 123, 255),
(122, 122, 255),
(121, 121, 255),
(120, 120, 255),
(119, 119, 255),
(118, 118, 255),
(117, 117, 255),
(116, 116, 255),
(115, 115, 255),
(114, 114, 255),
(113, 113, 255),
(112, 112, 255),
(111, 111, 255),
(110, 110, 255),
(109, 109, 255),
(108, 108, 255),
(107, 107, 255),
(106, 106, 255),
(105, 105, 255),
(104, 104, 255),
(103, 103, 255),
(102, 102, 255),
(101, 101, 255),
(100, 100, 255),
(99, 99, 255),
(98, 98, 255),
(97, 97, 255),
(96, 96, 255),
(95, 95, 255),
(94, 94, 255),
(93, 93, 255),
(92, 92, 255),
(91, 91, 255),
(90, 90, 255),
(89, 89, 255),
(88, 88, 255),
(87, 87, 255),
(86, 86, 255),
(85, 85, 255),
(84, 84, 255),
(83, 83, 255),
(82, 82, 255),
(81, 81, 255),
(80, 80, 255),
(79, 79, 255),
(78, 78, 255),
(77, 77, 255),
(76, 76, 255),
(75, 75, 255),
(74, 74, 255),
(73, 73, 255),
(72, 72, 255),
(71, 71, 255),
(70, 70, 255),
(69, 69, 255),
(68, 68, 255),
(67, 67, 255),
(66, 66, 255),
(65, 65, 255),
(64, 64, 255),
(63, 63, 255),
(62, 62, 255),
(61, 61, 255),
(60, 60, 255),
(59, 59, 255),
(58, 58, 255),
(57, 57, 255),
(56, 56, 255),
(55, 55, 255),
(54, 54, 255),
(53, 53, 255),
(52, 52, 255),
(51, 51, 255),
(50, 50, 255),
(49, 49, 255),
(48, 48, 255),
(47, 47, 255),
(46, 46, 255),
(45, 45, 255),
(44, 44, 255),
(43, 43, 255),
(42, 42, 255),
(41, 41, 255),
(40, 40, 255),
(39, 39, 255),
(38, 38, 255),
(37, 37, 255),
(36, 36, 255),
(35, 35, 255),
(34, 34, 255),
(33, 33, 255),
(32, 32, 255),
(31, 31, 255),
(30, 30, 255),
(29, 29, 255),
(28, 28, 255),
(27, 27, 255),
(26, 26, 255),
(25, 25, 255),
(24, 24, 255),
(23, 23, 255),
(22, 22, 255),
(21, 21, 255),
(20, 20, 255),
(19, 19, 255),
(18, 18, 255),
(17, 17, 255),
(16, 16, 255),
(15, 15, 255),
(14, 14, 255),
(13, 13, 255),
(12, 12, 255),
(11, 11, 255),
(10, 10, 255),
(9, 9, 255),
(8, 8, 255),
(7, 7, 255),
(6, 6, 255),
(5, 5, 255),
(4, 4, 255),
(3, 3, 255),
(2, 2, 255),
(1, 1, 255),
(0, 0, 255),
(0, 0, 255),
(0, 0, 253),
(0, 0, 251),
(0, 0, 250),
(0, 0, 248),
(0, 0, 247),
(0, 0, 245),
(0, 0, 243),
(0, 0, 242),
(0, 0, 240),
(0, 0, 239),
(0, 0, 237),
(0, 0, 235),
(0, 0, 234),
(0, 0, 232),
(0, 0, 231),
(0, 0, 229),
(0, 0, 228),
(0, 0, 226),
(0, 0, 224),
(0, 0, 223),
(0, 0, 221),
(0, 0, 220),
(0, 0, 218),
(0, 0, 216),
(0, 0, 215),
(0, 0, 213),
(0, 0, 212),
(0, 0, 210),
(0, 0, 208),
(0, 0, 207),
(0, 0, 205),
(0, 0, 204),
(0, 0, 202),
(0, 0, 201),
(0, 0, 199),
(0, 0, 197),
(0, 0, 196),
(0, 0, 194),
(0, 0, 193),
(0, 0, 191),
(0, 0, 189),
(0, 0, 188),
(0, 0, 186),
(0, 0, 185),
(0, 0, 183),
(0, 0, 181),
(0, 0, 180),
(0, 0, 178),
(0, 0, 177),
(0, 0, 175),
(0, 0, 174),
(0, 0, 172),
(0, 0, 170),
(0, 0, 169),
(0, 0, 167),
(0, 0, 166),
(0, 0, 164),
(0, 0, 162),
(0, 0, 161),
(0, 0, 159),
(0, 0, 158),
(0, 0, 156),
(0, 0, 155),
(0, 0, 155),
(0, 0, 156),
(0, 0, 158),
(0, 0, 159),
(0, 0, 161),
(0, 0, 162),
(0, 0, 164),
(0, 0, 166),
(0, 0, 167),
(0, 0, 169),
(0, 0, 170),
(0, 0, 172),
(0, 0, 174),
(0, 0, 175),
(0, 0, 177),
(0, 0, 178),
(0, 0, 180),
(0, 0, 181),
(0, 0, 183),
(0, 0, 185),
(0, 0, 186),
(0, 0, 188),
(0, 0, 189),
(0, 0, 191),
(0, 0, 193),
(0, 0, 194),
(0, 0, 196),
(0, 0, 197),
(0, 0, 199),
(0, 0, 201),
(0, 0, 202),
(0, 0, 204),
(0, 0, 205),
(0, 0, 207),
(0, 0, 208),
(0, 0, 210),
(0, 0, 212),
(0, 0, 213),
(0, 0, 215),
(0, 0, 216),
(0, 0, 218),
(0, 0, 220),
(0, 0, 221),
(0, 0, 223),
(0, 0, 224),
(0, 0, 226),
(0, 0, 228),
(0, 0, 229),
(0, 0, 231),
(0, 0, 232),
(0, 0, 234),
(0, 0, 235),
(0, 0, 237),
(0, 0, 239),
(0, 0, 240),
(0, 0, 242),
(0, 0, 243),
(0, 0, 245),
(0, 0, 247),
(0, 0, 248),
(0, 0, 250),
(0, 0, 251),
(0, 0, 253),
(0, 0, 255),
(0, 0, 255),
(1, 1, 255),
(2, 2, 255),
(3, 3, 255),
(4, 4, 255),
(5, 5, 255),
(6, 6, 255),
(7, 7, 255),
(8, 8, 255),
(9, 9, 255),
(10, 10, 255),
(11, 11, 255),
(12, 12, 255),
(13, 13, 255),
(14, 14, 255),
(15, 15, 255),
(16, 16, 255),
(17, 17, 255),
(18, 18, 255),
(19, 19, 255),
(20, 20, 255),
(21, 21, 255),
(22, 22, 255),
(23, 23, 255),
(24, 24, 255),
(25, 25, 255),
(26, 26, 255),
(27, 27, 255),
(28, 28, 255),
(29, 29, 255),
(30, 30, 255),
(31, 31, 255),
(32, 32, 255),
(33, 33, 255),
(34, 34, 255),
(35, 35, 255),
(36, 36, 255),
(37, 37, 255),
(38, 38, 255),
(39, 39, 255),
(40, 40, 255),
(41, 41, 255),
(42, 42, 255),
(43, 43, 255),
(44, 44, 255),
(45, 45, 255),
(46, 46, 255),
(47, 47, 255),
(48, 48, 255),
(49, 49, 255),
(50, 50, 255),
(51, 51, 255),
(52, 52, 255),
(53, 53, 255),
(54, 54, 255),
(55, 55, 255),
(56, 56, 255),
(57, 57, 255),
(58, 58, 255),
(59, 59, 255),
(60, 60, 255),
(61, 61, 255),
(62, 62, 255),
(63, 63, 255),
(64, 64, 255),
(65, 65, 255),
(66, 66, 255),
(67, 67, 255),
(68, 68, 255),
(69, 69, 255),
(70, 70, 255),
(71, 71, 255),
(72, 72, 255),
(73, 73, 255),
(74, 74, 255),
(75, 75, 255),
(76, 76, 255),
(77, 77, 255),
(78, 78, 255),
(79, 79, 255),
(80, 80, 255),
(81, 81, 255),
(82, 82, 255),
(83, 83, 255),
(84, 84, 255),
(85, 85, 255),
(86, 86, 255),
(87, 87, 255),
(88, 88, 255),
(89, 89, 255),
(90, 90, 255),
(91, 91, 255),
(92, 92, 255),
(93, 93, 255),
(94, 94, 255),
(95, 95, 255),
(96, 96, 255),
(97, 97, 255),
(98, 98, 255),
(99, 99, 255),
(100, 100, 255),
(101, 101, 255),
(102, 102, 255),
(103, 103, 255),
(104, 104, 255),
(105, 105, 255),
(106, 106, 255),
(107, 107, 255),
(108, 108, 255),
(109, 109, 255),
(110, 110, 255),
(111, 111, 255),
(112, 112, 255),
(113, 113, 255),
(114, 114, 255),
(115, 115, 255),
(116, 116, 255),
(117, 117, 255),
(118, 118, 255),
(119, 119, 255),
(120, 120, 255),
(121, 121, 255),
(122, 122, 255),
(123, 123, 255),
(124, 124, 255),
(125, 125, 255),
(126, 126, 255),
(127, 127, 255),
(128, 128, 255),
(129, 129, 255),
(130, 130, 255),
(131, 131, 255),
(132, 132, 255),
(133, 133, 255),
(134, 134, 255),
(135, 135, 255),
(136, 136, 255),
(137, 137, 255),
(138, 138, 255),
(139, 139, 255),
(140, 140, 255),
(141, 141, 255),
(142, 142, 255),
(143, 143, 255),
(144, 144, 255),
(145, 145, 255),
(146, 146, 255),
(147, 147, 255),
(148, 148, 255),
(149, 149, 255),
(150, 150, 255),
(151, 151, 255),
(152, 152, 255),
(153, 153, 255),
(154, 154, 255),
(155, 155, 255),
(156, 156, 255),
(157, 157, 255),
(158, 158, 255),
(159, 159, 255),
(160, 160, 255),
(161, 161, 255),
(162, 162, 255),
(163, 163, 255),
(164, 164, 255),
(165, 165, 255),
(166, 166, 255),
(167, 167, 255),
(168, 168, 255),
(169, 169, 255),
(170, 170, 255),
(171, 171, 255),
(172, 172, 255),
(173, 173, 255),
(174, 174, 255),
(175, 175, 255),
(176, 176, 255),
(177, 177, 255),
(178, 178, 255),
(179, 179, 255),
(180, 180, 255),
(181, 181, 255),
(182, 182, 255),
(183, 183, 255),
(184, 184, 255),
(185, 185, 255),
(186, 186, 255),
(187, 187, 255),
(188, 188, 255),
(189, 189, 255),
(190, 190, 255),
(191, 191, 255),
(192, 192, 255),
(193, 193, 255),
(194, 194, 255),
(195, 195, 255),
(196, 196, 255),
(197, 197, 255),
(198, 198, 255),
(199, 199, 255),
(200, 200, 255),
(201, 201, 255),
(202, 202, 255),
(203, 203, 255),
(204, 204, 255),
(205, 205, 255),
(206, 206, 255),
(207, 207, 255),
(208, 208, 255),
(209, 209, 255),
(210, 210, 255),
(211, 211, 255),
(212, 212, 255),
(213, 213, 255),
(214, 214, 255),
(215, 215, 255),
(216, 216, 255),
(217, 217, 255),
(218, 218, 255),
(219, 219, 255),
(220, 220, 255),
(221, 221, 255),
(222, 222, 255),
(223, 223, 255),
(224, 224, 255),
(225, 225, 255),
(226, 226, 255),
(227, 227, 255),
(228, 228, 255),
(229, 229, 255),
(230, 230, 255),
(231, 231, 255),
(232, 232, 255),
(233, 233, 255),
(234, 234, 255),
(235, 235, 255),
(236, 236, 255),
(237, 237, 255),
(238, 238, 255),
(239, 239, 255),
(240, 240, 255),
(241, 241, 255),
(242, 242, 255),
(243, 243, 255),
(244, 244, 255),
(245, 245, 255),
(246, 246, 255),
(247, 247, 255),
(248, 248, 255),
(249, 249, 255),
(250, 250, 255),
(251, 251, 255),
(252, 252, 255),
(253, 253, 255),
(254, 254, 255),
(255, 255, 255)
]

def rgb_to_ansi(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"

def smooth_gradient_ascii_chars(text, gradient_colors):
    chars = list(text)
    total_chars = len(chars)
    total_colors = len(gradient_colors)
    result = ""
    for i, char in enumerate(chars):
        if char == "\n":
            result += "\n"
            continue
        color_pos = i / max(1, total_chars - 1) * (total_colors - 1)
        lower = int(color_pos)
        upper = min(lower + 1, total_colors - 1)
        t = color_pos - lower
        r = int(gradient_colors[lower][0] + (gradient_colors[upper][0] - gradient_colors[lower][0]) * t)
        g = int(gradient_colors[lower][1] + (gradient_colors[upper][1] - gradient_colors[lower][1]) * t)
        b = int(gradient_colors[lower][2] + (gradient_colors[upper][2] - gradient_colors[lower][2]) * t)
        result += f"{rgb_to_ansi(r, g, b)}{char}\033[0m"
    return result


colorama.init(autoreset=True)

def nav_bar():
    print("\n\033[38;2;150;150;255m< Prev Page   |   Next Page >   |   q: Quit\033[0m")


def page_one():
    banner = """
 ██████   ██████            ███                ██████   ██████                               
░░██████ ██████            ░░░                ░░██████ ██████                                    
 ░███░█████░███   ██████   ████  ████████      ░███░█████░███   ██████  ████████   █████ ████
 ░███░░███ ░███  ░░░░░███ ░░███ ░░███░░███     ░███░░███ ░███  ███░░███░░███░░███ ░░███ ░███ 
 ░███ ░░░  ░███   ███████  ░███  ░███ ░███     ░███ ░░░  ░███ ░███████  ░███ ░███  ░███ ░███ 
 ░███      ░███  ███░░███  ░███  ░███ ░███     ░███      ░███ ░███░░░   ░███ ░███  ░███ ░███ 
 █████     █████░░████████ █████ ████ █████    █████     █████░░██████  ████ █████ ░░████████
░░░░░     ░░░░░  ░░░░░░░░ ░░░░░ ░░░░ ░░░░░    ░░░░░     ░░░░░  ░░░░░░  ░░░░ ░░░░░   ░░░░░░░░ 
============================================================================================================
"""

    menu = """
Made By: Evadefbi
Version: 1.1.2
Github: Evadefbi
See Credits!
Enjoy!
Telegram Bot : https://t.me/cstoolkit_bot

============================================================================================================
- Educational purposes only!
- I am NOT eligible for whatever u decide to use this info for!
============================================================================================================
Topics               Tools
 
1. Main Menu         9.  DNS Lookup
2. Infosec           10. IP Geolocation
3. Opsec             11. Hash Calculator
4. Osint             
5. Csint             
6. Encryption        
7. Learning         
8. Credits          

"""
    print(banner)
    print(smooth_gradient_ascii_chars(menu, gradient_colors))
    nav_bar()


def page_two():
    banner = """
 █████               ██████                                    
░░███               ███░░███                                   
 ░███  ████████    ░███ ░░░   ██████   █████   ██████   ██████ 
 ░███ ░░███░░███  ███████    ███░░███ ███░░   ███░░███ ███░░███
 ░███  ░███ ░███ ░░░███░    ░███ ░███░░█████ ░███████ ░███ ░░░ 
 ░███  ░███ ░███   ░███     ░███ ░███ ░░░░███░███░░░  ░███  ███
 █████ ████ █████  █████    ░░██████  ██████ ░░██████ ░░██████ 
░░░░░ ░░░░ ░░░░░  ░░░░░      ░░░░░░  ░░░░░░   ░░░░░░   ░░░░░░  
============================================================================================================

1. Download TMAC for mac address spoofing (https://technitium.com/tmac/)
2. Download ShutUp10++ to turn off trackers, data collection and more  (https://www.oo-software.com/en/shutup10)
3. Download bitdefender anti-virus (https://www.bitdefender.com/en-us/)
4. Download Comodo Firewall (https://www.comodo.com/antivirus-internet-security/#firewall)
5. Netlimiter (https://www.netlimiter.com/)
6. Bitwarden Password manager (https://bitwarden.com/)
=========================================Phone Setup =======================================================
1. Download GrapheneOS (https://grapheneos.org/)
2. Unlock phone bootloader to be able to installl the OS 
3. Follow the install instructions (https://grapheneos.org/install/web)
4. Download ProtonVPN (YES its secure), duckduckgo and Netgaurd (open-source firewall)
5. Download F-Droid (https://f-droid.org/en/) and Aurora Store (https://f-droid.org/en/packages/com.aurora.store/)
6. Use the phone number bought from smspool for  everything (https://www.smspool.net/)
"""
    print(smooth_gradient_ascii_chars(banner, gradient_colors))
    nav_bar()


def page_three():
    banner = """
     ███████                                       
  ███░░░░░███                                     
 ███     ░░███ ████████   █████   ██████   ██████ 
░███      ░███░░███░░███ ███░░   ███░░███ ███░░███
░███      ░███ ░███ ░███░░█████ ░███████ ░███ ░░░ 
░░███     ███  ░███ ░███ ░░░░███░███░░░  ░███  ███
 ░░░███████░   ░███████  ██████ ░░██████ ░░██████ 
   ░░░░░░░     ░███░░░  ░░░░░░   ░░░░░░   ░░░░░░  
               ░███                               
               █████                              
              ░░░░░    
============================================================================================================

1. Download Riseup VPN (https://riseup.net/en/vpn)
2. Download SoftEther VPN Client + VPN Gate Client Plugin (https://www.vpngate.net/en/download.aspx)    
3. Download Tor Browser (https://www.torproject.org/download/)
4. Use Wasabi wallet (https://wasabiwallet.io/#download) + Simpleswap (https://simpleswap.io/) to use crypto for online purchases
5. Use a cock.li (https://cock.li/) mail for everything 
6. Thunderbird mail client for cock.li (https://www.thunderbird.net/en-US/)
7. Use a different username for everything
8. Use temp phone numbers for verifications (https://www.smspool.net/)
9. Use a User-agent spoofer (https://addons.mozilla.org/en-CA/firefox/addon/user-agent-string-switcher/)
10. Download ProtonVPN Only for your mobile device! (YES its secure),
11. Onionshare for filesharing (https://onionshare.org/#download)
12. Exif data remover (https://exifcleaner.com/)
13. Messangers: Telegram (https://telegram.org/) Signal (https://signal.org/) session (https://getsession.org/) Zangi (Phone only) (https://zangi.com/)
14. uBlock (https://ublockorigin.com/)
"""
    print(smooth_gradient_ascii_chars(banner, gradient_colors))
    nav_bar()


def page_four():
    banner = """
    ███████             ███              █████   
  ███░░░░░███          ░░░              ░░███    
 ███     ░░███  █████  ████  ████████   ███████  
░███      ░███ ███░░  ░░███ ░░███░░███ ░░░███░   
░███      ░███░░█████  ░███  ░███ ░███   ░███    
░░███     ███  ░░░░███ ░███  ░███ ░███   ░███ ███
 ░░░███████░   ██████  █████ ████ █████  ░░█████ 
   ░░░░░░░    ░░░░░░  ░░░░░ ░░░░ ░░░░░    ░░░░░  
============================================================================================================

1. OSINT framework (https://osintframework.com/)
2. Shodan (https://www.shodan.io/)
3. TheHarvester (https://github.com/laramies/theHarvester)
4. Maltego (https://www.maltego.com/)
5. Spiderfoot (https://github.com/smicallef/spiderfoot)
6. Username Lookup (https://instantusername.com/)
7. Phone Lookup (https://www.truecaller.com/)
8. Media Lookup Tool (https://github.com/sherlock-project/sherlock)
9. Domain Lookup (https://www.whois.com/)
10. Port scanner (https://nmap.org/)
11. Network analizer (https://www.wireshark.org/)
12. IDCrawl FullName Lookup (https://www.idcrawl.com/)
13. Unter Email Lookup (https://hunter.io/)
14. WhoIs (https://who.is/)
15. Tineye Reverse Image (https://tineye.com)
16. Image Exif  Data Viewer (https://exif.tools/)
"""
    print(smooth_gradient_ascii_chars(banner, gradient_colors))
    nav_bar()


def page_five():
    banner = """
    █████████           ███              █████   
  ███░░░░░███         ░░░              ░░███    
 ███     ░░░   █████  ████  ████████   ███████  
░███          ███░░  ░░███ ░░███░░███ ░░░███░   
░███         ░░█████  ░███  ░███ ░███   ░███    
░░███     ███ ░░░░███ ░███  ░███ ░███   ░███ ███
 ░░█████████  ██████  █████ ████ █████  ░░█████ 
  ░░░░░░░░░  ░░░░░░  ░░░░░ ░░░░ ░░░░░    ░░░░░  
============================================================================================================

Disclaimer: These tools are NOT legal use with on ur own responsibility!

1. Csint Bot for personal information gathering (https://t.me/@OSINTHive_bot)
2. Oathnet (https://oathnet.org/)
3. Security Onion (https://securityonionsolutions.com/)
4. MISP (https://www.misp-project.org/)
5. Splunk (https://www.splunk.com/)
6. OpenCTI (https://github.com/OpenCTI-Platform/opencti?utm_source=chatgpt.com)
7. Wazuh (https://wazuh.com/)
8. BreachDirectory (https://breachdirectory.org/)
"""
    print(smooth_gradient_ascii_chars(banner, gradient_colors))
    nav_bar()

def page_six():
    banner = """
 ██████████                                                     █████     ███                     
░░███░░░░░█                                                    ░░███     ░░░                      
 ░███  █ ░  ████████    ██████  ████████  █████ ████ ████████  ███████   ████   ██████  ████████  
 ░██████   ░░███░░███  ███░░███░░███░░███░░███ ░███ ░░███░░███░░░███░   ░░███  ███░░███░░███░░███ 
 ░███░░█    ░███ ░███ ░███ ░░░  ░███ ░░░  ░███ ░███  ░███ ░███  ░███     ░███ ░███ ░███ ░███ ░███ 
 ░███ ░   █ ░███ ░███ ░███  ███ ░███      ░███ ░███  ░███ ░███  ░███ ███ ░███ ░███ ░███ ░███ ░███ 
 ██████████ ████ █████░░██████  █████     ░░███████  ░███████   ░░█████  █████░░██████  ████ █████
░░░░░░░░░░ ░░░░ ░░░░░  ░░░░░░  ░░░░░       ░░░░░███  ░███░░░     ░░░░░  ░░░░░  ░░░░░░  ░░░░ ░░░░░ 
                                           ███ ░███  ░███                                         
                                          ░░██████   █████                                        
                                           ░░░░░░   ░░░░░ 
============================================================================================================                                        

1. Veracrypt (https://veracrypt.jp/en/Home.html)'
2. 7-Zip (https://www.7-zip.org/) 
3. Cryptomator (https://cryptomator.org/)
"""
    print(smooth_gradient_ascii_chars(banner, gradient_colors))
    nav_bar()

def page_seven():
    banner = """
 █████                                                ███                     
░░███                                                ░░░                      
 ░███         ██████   ██████   ████████  ████████   ████  ████████    ███████
 ░███        ███░░███ ░░░░░███ ░░███░░███░░███░░███ ░░███ ░░███░░███  ███░░███
 ░███       ░███████   ███████  ░███ ░░░  ░███ ░███  ░███  ░███ ░███ ░███ ░███
 ░███      █░███░░░   ███░░███  ░███      ░███ ░███  ░███  ░███ ░███ ░███ ░███
 ███████████░░██████ ░░████████ █████     ████ █████ █████ ████ █████░░███████
░░░░░░░░░░░  ░░░░░░   ░░░░░░░░ ░░░░░     ░░░░ ░░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░███
                                                                      ███ ░███
                                                                     ░░██████ 
                                                                      ░░░░░░  
============================================================================================================ 

1. Tryhackme (https://tryhackme.com/)
2. HackTheBox (https://www.hackthebox.eu/)
3. HackerOne (https://www.hackerone.com/)
4. OverTheWire (https://overthewire.org/wargames/)
5. CyberDefenders (https://www.cyberdefenders.org/)
6. PortSwigger Web Security Academy (https://portswigger.net/web-security)
7. OWASP WebGoat (https://owasp.org/www-project-webgoat/)
8. Google Gruyere (https://google-gruyere.appspot.com/)
"""
    print(smooth_gradient_ascii_chars(banner, gradient_colors))
    nav_bar()

def real_dns_lookup(domain):
    results = {}
    record_types = ["A", "AAAA", "MX", "NS", "TXT"]
    for rtype in record_types:
        try:
            answers = dns.resolver.resolve(domain, rtype)
            results[rtype] = [str(rdata) for rdata in answers]
        except Exception:
            results[rtype] = None
    return results


def ip_to_geolocation(ip_address):
    """
    Returns geolocation information for a given IP address.
    """
    try:
        url = f"http://ip-api.com/json/{ip_address}"
        response = requests.get(url, timeout=5)
        data = response.json()

        if data['status'] == 'success':
            return {
                'IP': data.get('query', ''),
                'Country': data.get('country', ''),
                'Region': data.get('regionName', ''),
                'City': data.get('city', ''),
                'ZIP': data.get('zip', ''),
                'ISP': data.get('isp', ''),
                'Org': data.get('org', ''),
                'Latitude': data.get('lat', ''),
                'Longitude': data.get('lon', '')
            }
        else:
            return {'error': data.get('message', 'Unable to get location')}
    except Exception as e:
        return {'error': str(e)}

def detect_hash(hash_str):
    hash_str = hash_str.strip()
    hash_len = len(hash_str)
    possible = []

    # Hexadecimal check
    if re.fullmatch(r'[0-9a-fA-F]+', hash_str):
        if hash_len == 32:
            possible.append("MD5")
        if hash_len == 40:
            possible.append("SHA1")
        if hash_len == 56:
            possible.append("SHA224")
        if hash_len == 64:
            possible.append("SHA256")
        if hash_len == 96:
            possible.append("SHA384")
        if hash_len == 128:
            possible.append("SHA512")

    # Base64 check
    if re.fullmatch(r'[A-Za-z0-9+/=]+', hash_str):
        possible.append("Base64")

    if not possible:
        possible.append("Unknown / Invalid format")

    return possible


def page_eight():
    banner = """
 ██████████   ██████   █████  █████████     █████                         █████                          
░░███░░░░███ ░░██████ ░░███  ███░░░░░███   ░░███                         ░░███                           
 ░███   ░░███ ░███░███ ░███ ░███    ░░░     ░███         ██████   ██████  ░███ █████ █████ ████ ████████ 
 ░███    ░███ ░███░░███░███ ░░█████████     ░███        ███░░███ ███░░███ ░███░░███ ░░███ ░███ ░░███░░███
 ░███    ░███ ░███ ░░██████  ░░░░░░░░███    ░███       ░███ ░███░███ ░███ ░██████░   ░███ ░███  ░███ ░███
 ░███    ███  ░███  ░░█████  ███    ░███    ░███      █░███ ░███░███ ░███ ░███░░███  ░███ ░███  ░███ ░███
 ██████████   █████  ░░█████░░█████████     ███████████░░██████ ░░██████  ████ █████ ░░████████ ░███████ 
░░░░░░░░░░   ░░░░░    ░░░░░  ░░░░░░░░░     ░░░░░░░░░░░  ░░░░░░   ░░░░░░  ░░░░ ░░░░░   ░░░░░░░░  ░███░░░  
                                                                                                ░███     
                                                                                                █████    
                                                                                               ░░░░░
============================================================================================================
"""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')   
        print(smooth_gradient_ascii_chars(banner, gradient_colors))
        nav_bar()
        print("\n[ DNS LOOKUP TOOL ]")
        print("Press ENTER to skip • Type 'back' or '>' to return to menu\n")
        
        domain = input("Enter domain to lookup → ").strip()
        
        if domain.lower() in ["back", "b", ">"]:
            return
        
        if not domain:
            input("\n[!] No domain entered. Press ENTER to try again...")
            continue

        print("\nResolving", domain, "...\n")
        result = real_dns_lookup(domain)
        
        print("===== DNS RESULTS =====\n")
        for rtype, data in result.items():
            print(f"{Fore.CYAN}{rtype}:{Style.RESET_ALL}")
            if data:
                for entry in data:
                    print(f"   ➤ {entry}")
            else:
                print(f"   {Fore.RED}(No records found){Style.RESET_ALL}")
        print("\n" + "="*50 + "\n")
        
        input(f"{Fore.YELLOW}Press ENTER to do another lookup...{Style.RESET_ALL}")

def page_nine():
    banner = """
 █████ ███████████       █████████                                                                       
░░███ ░░███░░░░░███     ███░░░░░███                                                                      
 ░███  ░███    ░███    ███     ░░░   ██████   ██████                                                     
 ░███  ░██████████    ░███          ███░░███ ███░░███                                                    
 ░███  ░███░░░░░░     ░███    █████░███████ ░███ ░███                                                    
 ░███  ░███           ░░███  ░░███ ░███░░░  ░███ ░███                                                    
 █████ █████           ░░█████████ ░░██████ ░░██████                                                     
░░░░░ ░░░░░             ░░░░░░░░░   ░░░░░░   ░░░░░░ 
============================================================================================================
"""
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(smooth_gradient_ascii_chars(banner, gradient_colors))
        nav_bar()
        print("\n[ IP GEOLOCATION TOOL ]")
        print("Type 'back' or '>' to return to menu\n")
        
        ip_address = input("Enter IP address → ").strip()
        
        if ip_address.lower() in ["back", "b", ">"]:
            return
            
        if not ip_address:
            input("\n[!] No IP entered. Press ENTER to continue...")
            continue

        print(f"\nLooking up {ip_address}...\n")
        geo = ip_to_geolocation(ip_address)
        
        if 'error' in geo:
            print(f"{Fore.RED}[!] Error: {geo['error']}{Style.RESET_ALL}")
        else:
            print(f"{Fore.WHITE}=== Geolocation Results ==={Style.RESET_ALL}")
            print(f"IP           : {geo.get('IP', 'N/A')}")
            print(f"Country      : {geo.get('Country', 'N/A')}")
            print(f"Region       : {geo.get('Region', 'N/A')}")
            print(f"City         : {geo.get('City', 'N/A')}")
            print(f"ZIP          : {geo.get('ZIP', 'N/A')}")
            print(f"ISP          : {geo.get('ISP', 'N/A')}")
            print(f"Organization : {geo.get('Org', 'N/A')}")
            print(f"Lat/Long     : {geo.get('Latitude', 'N/A')}, {geo.get('Longitude', 'N/A')}")
        
        print("\n" + "="*50)
        input(f"\n{Fore.YELLOW}Press ENTER for another lookup...{Style.RESET_ALL}")

def page_ten():
    banner = """
 █████   █████                   █████           █████████            ████                               
░░███   ░░███                   ░░███           ███░░░░░███          ░░███                               
 ░███    ░███   ██████    █████  ░███████      ███     ░░░   ██████   ░███   ██████                      
 ░███████████  ░░░░░███  ███░░   ░███░░███    ░███          ░░░░░███  ░███  ███░░███                     
 ░███░░░░░███   ███████ ░░█████  ░███ ░███    ░███           ███████  ░███ ░███ ░░░                      
 ░███    ░███  ███░░███  ░░░░███ ░███ ░███    ░░███     ███ ███░░███  ░███ ░███  ███                     
 █████   █████░░████████ ██████  ████ █████    ░░█████████ ░░████████ █████░░██████                      
░░░░░   ░░░░░  ░░░░░░░░ ░░░░░░  ░░░░ ░░░░░      ░░░░░░░░░   ░░░░░░░░ ░░░░░  ░░░░░░
============================================================================================================
    """

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(smooth_gradient_ascii_chars(banner, gradient_colors))
        nav_bar()
        
        print(f"\n{Fore.WHITE}=== HASH / BASE64 DETECTOR ==={Style.RESET_ALL}")
        print("Enter a hash or Base64 string")
        print("Type 'back' or '>' to return to menu\n")
        
        user_input = input(f"{Fore.WHITE}Enter Hash → {Style.RESET_ALL}").strip()
        
        if user_input.lower() in ["back", "b", ">"]:
            return
            
        if not user_input:
            input(f"\n{Fore.RED}[!] Nothing entered. Press ENTER to try again...{Style.RESET_ALL}")
            continue

        print(f"\n{Fore.WHITE}Analyzing...{Style.RESET_ALL}\n")
        result = detect_hash(user_input)  
        
        if result:
            print(f"{Fore.WHITE}Detected possible type(s):{Style.RESET_ALL}")
            for r in result:
                print(f"   ➤ {Fore.WHITE}{r}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}No known hash type detected.{Style.RESET_ALL}")
        
        print("\n" + "="*60)
        input(f"\n{Fore.YELLOW}Press ENTER for another detection...{Style.RESET_ALL}")

def page_eleven():
    banner = """
    █████████                         █████  ███   █████           
  ███░░░░░███                       ░░███  ░░░   ░░███            
 ███     ░░░  ████████   ██████   ███████  ████  ███████    █████ 
░███         ░░███░░███ ███░░███ ███░░███ ░░███ ░░░███░    ███░░  
░███          ░███ ░░░ ░███████ ░███ ░███  ░███   ░███    ░░█████ 
░░███     ███ ░███     ░███░░░  ░███ ░███  ░███   ░███ ███ ░░░░███
 ░░█████████  █████    ░░██████ ░░████████ █████  ░░█████  ██████ 
  ░░░░░░░░░  ░░░░░      ░░░░░░   ░░░░░░░░ ░░░░░    ░░░░░  ░░░░░░  
============================================================================================================

╔════════════════════════════════════════════════════════════════╗
║  Made by: evadefbi                                             ║
║  Language: Python                                              ║
║  Discord: evadefbi                                             ║
║  Twitter(X): evadefbi                                          ║                                        
╚════════════════════════════════════════════════════════════════╝
"""
    print(smooth_gradient_ascii_chars(banner, gradient_colors))
    nav_bar()

def main():
    import os

    if os.name == "nt":
        os.system("mode con cols=137 lines=46")
    else:
        os.system("printf '\\033[8;45;137t'")

    current_page = 1
    total_pages = 11

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        if current_page == 1:
            page_one()
        elif current_page == 2:
            page_two()
        elif current_page == 3:
            page_three()
        elif current_page == 4:
            page_four()
        elif current_page == 5:
            page_five()
        elif current_page == 6:
            page_six()
        elif current_page == 7:
            page_seven()
        elif current_page == 8:
            page_eight()  
        elif current_page == 9:
            page_nine() 
        elif current_page == 10:
            page_ten() 
        elif current_page == 11:
            page_eleven() 

        choice = input("\nEnter < or > to switch pages (or q to quit): ").strip()
        if choice == '>':
            current_page += 1
            if current_page > total_pages:
                current_page = 1
        elif choice == '<':
            current_page -= 1
            if current_page < 1:
                current_page = total_pages
        elif choice.lower() == 'q':
            print("Exiting...")
            break
        else:
            print("Invalid input! Use <, >, or q.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()


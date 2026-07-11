%global tl_name spectralsequences
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3.3
Release:	%{tl_revision}.1
Summary:	Print spectral sequence diagrams using PGF/TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/spectralsequences
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spectralsequences.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/spectralsequences.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is a specialized tool built on top of PGF/TikZ for drawing
spectral sequences. It provides a powerful, concise syntax for
specifying the data of a spectral sequence, and then allows the user to
print various pages of spectral sequences, automatically choosing which
subset of the classes, differentials, and structure lines to display on
each page. It also handles most of the details of the layout. At the
same time, it is extremely flexible. spectralsequences is closely
integrated with TikZ to ensure that users can take advantage of as much
as possible of its expressive power. It is possible to turn off most of
the automated layout features and draw replacements using TikZ commands.
The package also provides a carefully designed error reporting system
intended to ensure that it is as clear as possible what is going wrong.


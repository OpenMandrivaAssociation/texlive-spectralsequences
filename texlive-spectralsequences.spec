Name:		texlive-spectralsequences
Version:	65667
Release:	1
Summary:	Print spectral sequence diagrams using PGF/TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/spectralsequences
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spectralsequences.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/spectralsequences.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is a specialized tool built on top of PGF/TikZ for
drawing spectral sequences. It provides a powerful, concise
syntax for specifying the data of a spectral sequence, and then
allows the user to print various pages of spectral sequences,
automatically choosing which subset of the classes,
differentials, and structure lines to display on each page. It
also handles most of the details of the layout. At the same
time, it is extremely flexible. spectralsequences is closely
integrated with TikZ to ensure that users can take advantage of
as much as possible of its expressive power. It is possible to
turn off most of the automated layout features and draw
replacements using TikZ commands. The package also provides a
carefully designed error reporting system intended to ensure
that it is as clear as possible what is going wrong.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/spectralsequences
%doc %{_texmfdistdir}/doc/latex/spectralsequences

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

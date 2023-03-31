Name:		texlive-pspicture
Version:	15878
Release:	2
Summary:	PostScript picture support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pspicture
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pspicture.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pspicture.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pspicture.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A replacement for LaTeX's picture macros, that uses PostScript
\special commands. The package is now largely superseded by
pict2e.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pspicture
%{_texmfdistdir}/tex/latex/pspicture
%doc %{_texmfdistdir}/doc/latex/pspicture
#- source
%doc %{_texmfdistdir}/source/latex/pspicture

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}

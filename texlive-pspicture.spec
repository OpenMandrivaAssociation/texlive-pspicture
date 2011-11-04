# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/pspicture
# catalog-date 2007-03-11 16:56:01 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-pspicture
Version:	20070311
Release:	1
Summary:	PostScript picture support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pspicture
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pspicture.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pspicture.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pspicture.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
A replacement for LaTeX's picture macros, that uses PostScript
\special commands. The package is now largely superseded by
pict2e.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pspicture/pspicture.ps
%{_texmfdistdir}/tex/latex/pspicture/pspicture.sty
%doc %{_texmfdistdir}/doc/latex/pspicture/README
%doc %{_texmfdistdir}/doc/latex/pspicture/pspicture.pdf
#- source
%doc %{_texmfdistdir}/source/latex/pspicture/pspicture.dtx
%doc %{_texmfdistdir}/source/latex/pspicture/pspicture.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
